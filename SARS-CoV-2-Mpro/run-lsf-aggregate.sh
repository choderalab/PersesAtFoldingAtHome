#!/bin/bash

# Dock COVID Moonshot compounds in parallel

#BSUB -W 3:00
#BSUB -R "rusage[mem=2]"
#BSUB -n 1
#BSUB -R "span[ptile=1]"
#BSUB -q cpuqueue
#BSUB -o %J.aminopyridines-aggregate.out
#BSUB -J "aminopyridines-aggregate"

echo "Job $JOBID/$NJOBS"

echo "LSB_HOSTS: $LSB_HOSTS"

source ~/.bashrc

conda activate perses

export PREFIX="aminopyridines_for_chodera_lab"

# Extract sorted docking results
python 03-aggregate-docking-results.py --molecules $PREFIX.csv --docked $PREFIX-docked --output $PREFIX-docked-justscore.csv --clean
python 03-aggregate-docking-results.py --molecules $PREFIX.csv --docked $PREFIX-docked --output $PREFIX-docked.csv
python 03-aggregate-docking-results.py --molecules $PREFIX.csv --docked $PREFIX-docked --output $PREFIX-docked.sdf
python 03-aggregate-docking-results.py --molecules $PREFIX.csv --docked $PREFIX-docked --output $PREFIX-docked.pdb

