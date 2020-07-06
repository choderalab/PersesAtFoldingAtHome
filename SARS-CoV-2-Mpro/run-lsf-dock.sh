#!/bin/bash

# Dock COVID Moonshot compounds in parallel

#BSUB -W 3:00
#BSUB -R "rusage[mem=2]"
#BSUB -n 1
#BSUB -R "span[ptile=1]"
#BSUB -q cpuqueue
#BSUB -o %J.aminopyridines-dock.out
#BSUB -J "aminopyridines-dock[1-242]"

echo "Job $JOBID/$NJOBS"

echo "LSB_HOSTS: $LSB_HOSTS"

source ~/.bashrc

source activate perses

export PREFIX="aminopyridines_for_chodera_lab"

let JOBID=$LSB_JOBINDEX-1
python 02-dock-and-prep.py --receptors receptors/monomer --molecules $PREFIX.csv --index $JOBID --output $PREFIX-docked 
