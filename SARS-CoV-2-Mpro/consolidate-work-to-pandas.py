#!/usr/bin/env python

"""
Extract final work values to a single pandas dataframe
"""

import os

projects = {
    'complex' : 13418,
    'solvent' : 13419,
    }

NUM_EXPECTED_WORK = 4001
NUM_EXPECTED_WORK = 401
NUM_EXPECTED_WORK = 41

phases = list(projects.keys())

basepaths = [
    '/home/server/server2/data/SVR314342810/',
    ]

import datetime
timestamp = datetime.datetime.now()

def get_results(PROJ):
    """
    Get all result directories for a given project

    Parameters
    ----------
    PROJ : str
        PROJ, such as 'PROJ13400'

    Returns
    -------
    results : dict
        results[path] = (PROJ,RUN,CLONE,GEN) where path is the results directory
    """
    from tqdm import tqdm
    
    # Make a list of all results packets paths from all locations
    paths = list()
    from glob import glob # glob takes forever on S3 file gateway, so we don't use it
    import os
    import re
    for basepath in basepaths:
        #paths += glob(f'{basepath}/{PROJ}/RUN*/CLONE*/results*')
        print(basepath)
        for RUN in tqdm(os.listdir(f'{basepath}/{PROJ}')):
            if not re.search('RUN', RUN): continue
            for CLONE in os.listdir(f'{basepath}/{PROJ}/{RUN}'):
                if not re.search('CLONE', CLONE): continue
                for result in os.listdir(f'{basepath}/{PROJ}/{RUN}/{CLONE}'):
                    if re.search('results\d+$', result):
                        path = f'{basepath}/{PROJ}/{RUN}/{CLONE}/{result}'
                        paths.append(path)

    # Construct results
    results = dict()
    nfailures = 0
    nsuccesses = 0
    for path in tqdm(paths):
        match = re.search('(?P<RUN>RUN\d+)/(?P<CLONE>CLONE\d+)/results(?P<GEN>\d+)$', path)

        # Skip failures
        if match is None:
            nfailures += 1
            continue
        nsuccesses += 1
        
        RUN = match.group('RUN')
        CLONE = match.group('CLONE')
        GEN = f"{match.group('GEN')}"

        results[path] = (PROJ,RUN,CLONE,GEN)

    failure_rate = float(nfailures) / float(nfailures + nsuccesses)
    print(f'{PROJ} : {nsuccesses} successes, {nfailures} failures ({failure_rate*100:.3}% failure rate)')
        
    return results
            
# Get all results directories
print('Gathering all results packets...')
results = dict()
for phase in phases:
    PROJ = f'PROJ{projects[phase]}'
    print(PROJ)
    results.update(get_results(PROJ))
            
def get_work(path):
    import pandas as pd
    import os
    import numpy as np
    import re
    
    match = re.search('(?P<PROJ>PROJ\d+)/(?P<RUN>RUN\d+)/(?P<CLONE>CLONE\d+)/results(?P<GEN>\d+)$', path)
    PROJ = match.group('PROJ')
    RUN = match.group('RUN')
    CLONE = match.group('CLONE')
    GEN = f"GEN{match.group('GEN')}"

    # Read csvfile
    try:
        csvfile = os.path.join(path, 'globals.csv')
        # Read the CSV file contents
        with open(csvfile, 'rt') as infile:
            lines = infile.readlines()
        # Keep track of the last header line
        header_line_number = 0
        for line_number, line in enumerate(lines):
            if 'kT' in line:
                header_line_number = line_number
        # Create pandas data frame
        with open(csvfile, 'rt') as infile:
            df = pd.read_csv(infile, header=header_line_number)
        # Drop duplicates
        df.drop_duplicates(inplace=True)
        # Correct work values
        kT = df['kT'].to_numpy(dtype=np.float32)[0]
        df['protocol_work'] /= kT
        df['Enew'] /= kT
        # Filter columns
        df = df[['Step', 'Time','lambda', 'Enew', 'protocol_work']]        
        # Perform sanity checks
        # TODO: Determine length automatically from first example
        protocol_work = df['protocol_work'].to_numpy()
        assert len(protocol_work) == NUM_EXPECTED_WORK, f'Expected {NUM_EXPECTED_WORK} work values, found {len(protocol_work)} : {path}'
        # Check total number of steps
        step = df['Step'].to_numpy()
        nsteps = step[-1] - step[0]
        NSTEPS_EXPECTED = 1000000
        assert nsteps == NSTEPS_EXPECTED, f'Expected {NSTEPS_EXPECTED} steps, found {nsteps} : {path}'
        # Return the dataframe
        return (PROJ, RUN, CLONE, GEN, df)
    except Exception as e:
        print(f'Exception for {csvfile}:', e)
        return None

# Process all paths
from multiprocessing import Pool
pool = Pool(processes=8)
print('Reading all work trajectories...')
import pandas as pd
from tqdm import tqdm
import numpy as np

CHECKPOINT_FREQUENCY = 10000

npaths = len(results)
master_df = pd.DataFrame(index=np.arange(0, npaths), columns=['PROJ', 'RUN', 'CLONE', 'GEN', 'forward_work', 'reverse_work', 'forward_final_potential', 'reverse_final_potential'])
results_processed = 0
for result in tqdm(pool.imap_unordered(get_work, results), total=len(results)):
    if result is not None:
        # Process result
        PROJ, RUN, CLONE, GEN, df = result
        protocol_work = df['protocol_work'].to_numpy()
        Enew = df['Enew'].to_numpy()
        forward_work = protocol_work[20] - protocol_work[10]
        reverse_work = protocol_work[40] - protocol_work[30]
        forward_final_potential = Enew[20]
        reverse_final_potential = Enew[40]
        # Add row to dataframe
        row = [PROJ, RUN, CLONE, GEN, forward_work, reverse_work, forward_final_potential, reverse_final_potential]
        master_df.loc[results_processed] = row
        # Increment counter
        results_processed += 1
        # Checkpoint periodically
        #if results_processed % CHECKPOINT_FREQUENCY == 0:
        #    master_df.to_pickle('work.pkl.bz2')

master_df.to_pickle('work-13418.pkl.bz2')
