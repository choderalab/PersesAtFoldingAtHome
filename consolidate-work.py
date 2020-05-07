#!/usr/bin/env python

"""
Extract work values in to numpy arrays
"""

import os

projects = {
    'complex' : 13404,
    'solvent' : 13405,
    }

NUM_EXPECTED_WORK = 4001

phases = list(projects.keys())

basepaths = [
    '/home/server/server2/data/SVR314342810/',
    '/archive/SVR314342810/',
    ]

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
    from glob import glob
    import re
    for basepath in basepaths:
        paths += glob(f'{basepath}/{PROJ}/RUN*/CLONE*/results*')

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
        GEN = f"GEN{match.group('GEN')}"

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
    PROJ, RUN, CLONE, GEN = results[path]

    # Read csvfile
    try:
        csvfile = os.path.join(path, 'globals.csv')
        df = pd.read_csv(csvfile)
        time = df['Time'].to_numpy(dtype=np.float32)
        lambda_t = df['lambda'].to_numpy(dtype=np.float32)
        kT = df['kT'].to_numpy(dtype=np.float32)[0]
        protocol_work = df['protocol_work'].to_numpy()
        # TODO: Determine length automatically from first example
        assert len(protocol_work) == NUM_EXPECTED_WORK, f'Expected {NUM_EXPECTED_WORK} work values, found {len(protocol_work)}'
        return (PROJ, RUN, CLONE, GEN, protocol_work / kT)
    except Exception as e:
        print(e)
        return None
        
# Now gather all works
from multiprocessing import Pool
pool = Pool(processes=8)
print('Reading all work trajectories...')
import pandas as pd
from tqdm import tqdm
work = dict() # work[PROJ][RUN][CLONE][GEN] is a numpy array of [Tmax] work values, in units of kT
for result in tqdm(pool.imap_unordered(get_work, results), total=len(results)):
    if result is None:
        continue
    
    PROJ, RUN, CLONE, GEN, protocol_work = result
        
    if PROJ not in work:
        work[PROJ] = dict()
    if RUN not in work[PROJ]:
        work[PROJ][RUN] = dict()
    if CLONE not in work[PROJ][RUN]:
        work[PROJ][RUN][CLONE] = dict()
    
    work[PROJ][RUN][CLONE][GEN] = protocol_work
        
# Pickle work
filename = 'work.pkl.bz2'
print(f'Writing work to {filename}...')
import pickle
import bz2
with bz2.BZ2File(filename, 'w') as outfile: 
    pickle.dump(work, outfile)

