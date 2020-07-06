perses on Folding@home free energy calculations for COVID Moonshot

## Manifest

Source compounds:
* `aminopyridines_for_chodera_lab.csv` - aminopyridine series (2 July 2020)

Docking:
* `run-lsf-dock.sh` - dock compounds
* `run-lsf-aggregate.sh` - aggregate docking results
* `aminopyridines_for_chodera_lab-docked.csv` - docked compound scores and data from original CSV
* `aminopyridines_for_chodera_lab-docked.sdf` - docked compound geometries in appropriate protonation states
* `aminopyridines_for_chodera_lab-docked.pdb` - PDB file of SDF 
* `aminopyridines_for_chodera_lab-docked/` - docked compounds prior to aggregation
* `aminopyridines_for_chodera_lab-docked-justscore.csv` - just the scores

Setup:
* `create-json.py` - script to set up which ligand transformations will be carried out
* `aminopyridines 2020-07-04.json` - output of this script
* `backtesting.yaml` - template for perses YAML
* `submit-ligpairs.sh` - LSF batch queue script to launch automated setup
* `run.py` - script executed by batch queue script
* `receptors/` - source structures from https://github.com/FoldingAtHome/covid-moonshot/tree/master/receptors
