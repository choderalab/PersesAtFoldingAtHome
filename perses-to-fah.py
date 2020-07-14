#!/usr/bin/env python

"""
Convert perses project to FAH

# prereqs
conda config --add channels omnia --add channels conda-forge
conda create -n perses python3.7 perses tqdm dicttoxml
pip uninstall --yes openmmtools 
pip install git+https://github.com/choderalab/openmmtools.git
"""
import os

import simtk
import openmmtools

# PARAMETERS
targets = ['cdk2']
projects = {
    'complex' : '13400',
    'solvent' : '13401',
}
phases = ['complex', 'solvent']

# Alchemical functions
x = 'lambda'
alchemical_functions = {
                         'lambda_sterics_core': x,
                         'lambda_electrostatics_core': x,
                         'lambda_sterics_insert': f"select(step({x} - 0.5), 1.0, 2.0 * {x})",
                         'lambda_sterics_delete': f"select(step({x} - 0.5), 2.0 * ({x} - 0.5), 0.0)",
                         'lambda_electrostatics_insert': f"select(step({x} - 0.5), 2.0 * ({x} - 0.5), 0.0)",
                         'lambda_electrostatics_delete': f"select(step({x} - 0.5), 1.0, 2.0 * {x})",
                         'lambda_bonds': x,
                         'lambda_angles': x,
                         'lambda_torsions': x}

# Create integrator
from simtk import openmm, unit
from openmmtools.integrators import PeriodicNonequilibriumIntegrator
temperature = 298*unit.kelvin
pressure = 1*unit.atmospheres
collision_rate = 1.0/unit.picoseconds
timestep = 4*unit.femtoseconds
nsteps_per_ps = 250 # number of steps per picosecond
nsteps_per_ns = 1000*nsteps_per_ps
nsteps_eq = nsteps_per_ns
nsteps_neq = nsteps_per_ns
integrator = PeriodicNonequilibriumIntegrator(nsteps_eq=nsteps_eq, nsteps_neq=nsteps_neq,
                                              temperature=temperature, collision_rate=collision_rate, timestep=timestep,
                                              alchemical_functions=alchemical_functions, splitting="V R H O R V")

def create_core_parameters(phase):
    """
    """
    # Create core.xml
    nsteps_per_cycle = 2*nsteps_eq + 2*nsteps_neq
    
    if phase == 'complex':
        ncycles = 2
    if phase == 'solvent':
        ncycles = 20
    
    core_parameters = {
        'numSteps' : ncycles * nsteps_per_cycle,
        'xtcFreq' : nsteps_per_ns,
        'precision' : 'mixed',
        'globalVarFilename' : 'globals.csv',
        'globalVarFreq' : nsteps_per_ps,
    }

    return core_parameters

def deserialize(filename):
    if filename.endswith('.gz'):
        import gzip
        with gzip.open(filename, 'rt') as infile:
            return openmm.XmlSerializer.deserialize(infile.read())
    else:
        with open(filename, 'rt') as infile:
            return openmm.XmlSerializer.deserialize(infile.read())
        
def serialize(filename, thing):
    if filename.endswith('.gz'):
        import gzip
        with gzip.open(filename, 'wt') as outfile:
            outfile.write(openmm.XmlSerializer.serialize(thing))
    else:
        with open(filename, 'wt') as outfile:
            outfile.write(openmm.XmlSerializer.serialize(thing))
        
def minimize_and_equilibrate(system, state, nsteps=10):
    import tqdm
    from openmmtools.integrators import LangevinIntegrator
    #equil_integrator = LangevinIntegrator(temperature, collision_rate, timestep)
    nequil = 25
    nsteps_per_equil_iteration = 250
    equil_integrator = PeriodicNonequilibriumIntegrator(nsteps_eq=(nequil+1)*nsteps_per_equil_iteration, nsteps_neq=nsteps_neq,
                                              temperature=temperature, collision_rate=collision_rate, timestep=timestep,
                                              alchemical_functions=alchemical_functions, splitting="V R H O R V")

    has_barostat = False
    for force in system.getForces():
        if force.__class__.__name__ == 'MonteCarloBarostat':
            has_barostat = True
            force.setDefaultPressure(pressure)
            force.setDefaultTempreature(temperature)
    if not has_barostat:
        barostat = openmm.MonteCarloBarostat(pressure, temperature)
        system.addForce(barostat)
    
    platform = openmm.Platform.getPlatformByName('CUDA')
    platform.setPropertyDefaultValue('Precision', 'mixed')
    platform.setPropertyDefaultValue('DeterministicForces', 'true')
    context = openmm.Context(system, equil_integrator, platform)
    context.setPeriodicBoxVectors(*state.getPeriodicBoxVectors())
    context.setPositions(state.getPositions())

    # Set alchemical parameters to lambda = 0
    equil_integrator.reset() # sets step = -1
    equil_integrator.step(1) # resets all alchemical and context parameters to lambda = 0

    # Minimize
    nminimize = 5
    from tqdm import tqdm
    print('  minimizing: ')
    initial_energy = context.getState(getEnergy=True).getPotentialEnergy()
    print(f'    initial energy is {initial_energy}')
    if initial_energy > 0.0*unit.kilocalories_per_mole:
        raise Exception('Initial energy is positive, so skipping minimization')
    for iteration in tqdm(range(nminimize)):
        openmm.LocalEnergyMinimizer.minimize(context, 0.0, 1)
    print(f'    final energy is {context.getState(getEnergy=True).getPotentialEnergy()}')

    # Equilibrate
    print('  equilibrating: ')
    from tqdm import tqdm
    for iteration in tqdm(range(nequil)):
        context.setVelocitiesToTemperature(temperature)
        equil_integrator.step(nsteps_per_equil_iteration)
        equil_integrator.reset()
    context.setVelocitiesToTemperature(temperature)

    # Get final state
    # TODO: Get parameters too? Do we have to reconstitute in production integrator?
    state = context.getState(getPositions=True, getVelocities=True, getForces=True, getEnergy=True)

    # Clean up
    del context, equil_integrator

    return system, state

def test_simulation(rundir):
    """
    Test the simulations from serialized files.
    """
    print(f'Testing {rundir}...')
    system = deserialize(f'{rundir}/system.xml')
    state = deserialize(f'{rundir}/state.xml')
    test_integrator = deserialize(f'{rundir}/integrator.xml')
    context = openmm.Context(system, test_integrator)
    context.setState(state)
    nsteps = 10
    test_integrator.step(nsteps)
    print(f'  energy is {context.getState(getEnergy=True).getPotentialEnergy()} after {nsteps} steps of simulation')
    del context, test_integrator

successful_complexes = set()
for phase in ['complex', 'solvent']:
    # TODO: Check if csv file already exists and load run info if so
    runs = list()

    for target in targets:
        print(target, phase)

        # Get a list of all transformations
        from glob import glob
        edgedirs = glob(f'{target}/lig*to*')
        print(edgedirs)

        for edgedir in edgedirs:
            print('')
            print(f'{target} {phase} {edgedir}')

            if phase == 'solvent':
                if edgedir not in successful_complexes:
                    print('  skipping solvent leg because complex was unsuccessful')
                    continue
        
            # Extract reference and target ligand indices
            import re
            m = re.search('lig(?P<reference_ligand_index>\d+)to(?P<target_ligand_index>\d+)', edgedir)
            reference_ligand_index = int(m.group('reference_ligand_index'))
            target_ligand_index = int(m.group('target_ligand_index'))
            
            import os
            project = projects[phase]
            run_index = len(runs)
            rundir = f'{project}/RUNS/RUN{run_index}'

            if not os.path.exists(f'{rundir}/system.xml'):
    
                # Read system and state
                print('  deserializing...')
                system = deserialize(f'{edgedir}/xml/{phase}-hybrid-system.gz')
                state = deserialize(f'{edgedir}/xml/{phase}-hybrid-old-state.gz')

                # Minimize and equilibrate
                try:
                    system, state = minimize_and_equilibrate(system, state)
                except Exception as e:
                    with open('exceptions.out', 'a') as outfile:
                        outfile.write(f'{target} {phase} {edgedir}: ')
                        outfile.write(str(e) + '\n')
                        continue

                # Copy files into RUN directory
                print(f'Staging {rundir} from {edgedir}...')
                os.makedirs(rundir, exist_ok=True)
                serialize(f'{rundir}/integrator.xml', integrator)
                serialize(f'{rundir}/state.xml', state)
                serialize(f'{rundir}/system.xml', system)

                # Serialize core.xml
                import dicttoxml
                with open(f'{rundir}/core.xml', 'wb') as outfile:
                    core_parameters = create_core_parameters(phase)
                    xml = dicttoxml.dicttoxml(core_parameters)
                    outfile.write(xml)
    
                # Test
                try:
                    test_simulation(rundir)
                except Exception as e:
                    print(e)

            if phase == 'complex':
                successful_complexes.add(edgedir)
                
            # Store info
            run_info = dict()
            run_info['rundir'] = rundir
            run_info['target'] = target
            run_info['edgedir'] = edgedir
            run_info['reference_ligand_index'] = reference_ligand_index
            run_info['target_ligand_index'] = target_ligand_index

            runs.append(run_info)
    
    # Write CSV file
    print('Writing CSV file...')
    import csv
    project = projects[phase]
    with open(f'{project}/run-index.csv', 'w') as csvfile:
        fieldnames = ['rundir', 'target', 'edgedir', 'reference_ligand_index', 'target_ligand_index']
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for run_info in runs:
            csvwriter.writerow(run_info)
    
