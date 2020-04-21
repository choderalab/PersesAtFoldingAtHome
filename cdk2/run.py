import yaml 
import sys
import itertools
import os

def run_relative_perturbation(ligA, ligB,tidy=True):
    print('Starting relative calcluation of ligand {} to {}'.format(ligA,ligB))
    trajectory_directory = 'lig{}to{}'.format(ligA,ligB) 
    new_yaml = 'vanilla_{}to{}.yaml'.format(ligA,ligB) 
    
    # rewrite yaml file
    with open('vanilla_setup.yaml', "r") as yaml_file:
        options = yaml.load(yaml_file)
    options['old_ligand_index'] = ligA
    options['new_ligand_index'] = ligB
    options['trajectory_directory'] = trajectory_directory
    with open(new_yaml, 'w') as outfile:
        yaml.dump(options, outfile)
    
    # run the simulation
    os.system('perses-relative {}'.format(new_yaml))

    print('Relative calcluation of ligand {} to {} complete'.format(ligA,ligB))

    if tidy:
        os.remove(new_yaml)

    return

# work out which ligand pair to run
ligand_pairs = [(13, 7), (14, 15), (14, 8), (14, 13), (12, 15), (9, 15), (9, 3), (1, 9), (1, 11), (6, 9), (0, 9), (0, 11), (11, 4), (7, 3), (7, 8), (10, 2), (10, 9), (3, 12), (5, 9), (5, 15), (2, 3), (2, 4), (2, 6), (2, 11), (2, 15)]
ligand1, ligand2 = ligand_pairs[int(sys.argv[1])-1] # jobarray starts at 1 

#running forwards
run_relative_perturbation(ligand2, ligand1)
