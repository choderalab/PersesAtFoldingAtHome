import numpy as np
import json
import math
import itertools

master_dict = {}
ff = 'openff-1.2.0'
# protein_dict = {'Series5':'protein.pdb'}
series_name = 'aminopyridines 2020-07-04'
ligand_dict = {series_name:'aminopyridines_for_chodera_lab-docked.sdf'}
n_ligands = {series_name:222}

index = 420 # starting index
i = 0
for protein in ['receptors/monomer/Mpro-x0434-protein.pdb', 'receptors/monomer/Mpro-x0434-protein-thiolate.pdb']:
    for series in [series_name]:
        for j in range(1, n_ligands[series]):
    #         expt = target.experimental[pair[1]]-target.experimental[pair[0]]
            master_dict[index] = {'target':'backtesting','start':i,'end':j,
                                  'protein':protein,'ligand':ligand_dict[series],'ff':ff,
                                           'directory':f'RUN{index-1}','JOBID':index}
            index+=1
            master_dict[index] = {'target':'backtesting','start':j,'end':i,
                                  'protein':protein,'ligand':ligand_dict[series],'ff':ff,
                                           'directory':f'RUN{index-1}','JOBID':index}
            index+=1

with open(f"{series_name}.json", "w") as f:
    json.dump(master_dict, f, sort_keys=True, indent=4, separators=(',', ': '))
