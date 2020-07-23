# PersesAtFoldingAtHome


## Documentation of pipeline:

See all the [details of running a FAH server and setting up new projects first](https://github.com/foldingathome/fah-docs/wiki).

- [ ] First, the project manager sets up one or more protein PDB files and ligand SDF files
- [ ] We select a FAH complex project ID (`complex_projid`) and solvent project ID (`solvent_projid`) pair from the [reserved set of projects wiki](https://github.com/FoldingAtHome/fah-docs/wiki/Project-numbers). FAH is limited to 65536 projects over its entire lifetime, so we have to conserve project numbers when possible. The complex project will have a large number of total atoms (~80K) and the solvent project will have a small number (~4K) where we can keep adding `RUN`s for new systems or new transformations as long as they fit in the simulation boxes.
- [ ] When we want to add one or more new ligands to the set (e.g. by adding rows to the [COVID Moonshot Compound Tracker](https://covid.postera.ai/covid/submissions/compounds), which can be [downloaded via the "Export CSV" button](https://covid.postera.ai/covid/submissions.csv) or at the associated [master GitHub repo](https://github.com/postera-ai/COVID_moonshot_submissions) in a [CSV file](https://github.com/postera-ai/COVID_moonshot_submissions/blob/master/covid_submissions_all_info.csv)), we convert the SMILES for the ligand into actual 3D molecules, expanding stereochemistry and store in SDF, and then identify which reference protein PDB structures we will create alchemical transformations (one transformation per FAH `RUN` for).  [JDC will provide script for this part, still being worked out.]
Hannah currently uses a [script](https://github.com/choderalab/PersesAtFoldingAtHome/blob/master/SARS-CoV-2-Mpro/create-json.py) to populate a [JSON file](https://github.com/choderalab/PersesAtFoldingAtHome/blob/master/SARS-CoV-2-Mpro/aminopyridines%202020-07-04.json), but we don't need to use this format (unless Hannah says otherwise).
- [ ] Hannah uses a script to parallelize the setup of individual transformations in parallel using our cluster (`lilac`) via an [LSF bash script](https://github.com/choderalab/PersesAtFoldingAtHome/blob/master/SARS-CoV-2-Mpro/submit-ligpairs.sh) and a [python `run.py`](https://github.com/choderalab/PersesAtFoldingAtHome/blob/master/SARS-CoV-2-Mpro/run.py).
- [ ] To set up a single ligand transformation (`i -> j`), we run the `perses` command-line entry point `perses-fah config.yaml`, where `config.yaml` looks like this:
```yaml
protein_pdb: CDK2_protein.pdb
ligand_file: CDK2_ligands_shifted.sdf
old_ligand_index: 0
new_ligand_index: 1
forcefield_files:
    - amber/ff14SB.xml # ff14SB protein force field
    - amber/tip3p_standard.xml # TIP3P and recommended monovalent ion parameters
    - amber/tip3p_HFE_multivalent.xml # for divalent ions
    - amber/phosaa10.xml # HANDLES THE TPO
atom_expression:
    - IntType
bond_expression:
    - DefaultBonds
complex_projid: 13418
solvent_projid: 13419
```
In practice, this is generated from a JSON file with a script called `run.py`.
This requires a GPU to be practical (e.g. GTX 1080).

This will create files `{complex_projid}/RUNS/RUN/...` and `{solvent_projid}/RUNS/RUN/...` with the directories populated with some metadata important to retain plus `{system,state,integrator,core}.xml` (or `.bz2` or `.gz` compressed versions thereof).
- [ ] `rsync` these files over to `server@aws3.foldingathome.org:/projects/available/covid-moonshot/`. It's OK to add more RUNs dynamically, but they must be compact and sequentially numbered from `RUN0`. The `{projid}` directory will be symlinked to `/home/server/server2/projects/{projid}` for the server to discover it.
- [ ] The `{projid}` directory will contain a `project.xml` file that looks like this:
```XML
<project type="OPENMM_22" id="13418">
  <gpu/>
  <min-core-version v="0.0.11"/>

  <job-priority v="queue-count gen clone run"/>

  <runs v="759"/>
  <clones v="100"/>
  <gens v="6"/>
  <atoms v="89709"/>

  <timeout v="1.0"/>
  <deadline v="2.0"/>
  <!-- <k-factor v="0.75"/> -->
  <!-- <stats-credit v="53245"/> -->  
  <!-- <stats-credit v="70000"/> --> <!-- SARS-CoV-2 Mpro -->
  <stats-credit v="55000"/>

  <send>
    $home/core.xml
    $home/RUNS/RUN$run/system.xml.bz2
    $home/RUNS/RUN$run/integrator.xml
    state.xml.bz2
  </send>

  <create-command>
    ln -s -f $home/RUNS/RUN$run/state.xml.bz2 $jobdir/state.xml.bz2
  </create-command>

  <next-gen-command>
    mv -f $results/checkpointState.xml.bz2 $jobdir/state.xml.bz2
  </next-gen-command>

  <!-- Don't copy to S3 storage gateway -->
  <archive-command>
    /usr/bin/true
  </archive-command>

</project>
```
- [ ] edit `{projid}/project.xml` for each project and increment the `runs` tag value to reflect the new runs
- [ ] restart the FAH server with `sudo service fah-work restart` as the `server` user on `aws3.foldingathome.org`, and check `~/server2/log.txt` that the server successfully restarts
- [ ] if this is a new project, some manual benchmarking and assignment server stuff needs to be done: see [here](https://github.com/FoldingAtHome/fah-docs/wiki/Set-up-an-OpenMM-%28GPU%29-Project) and subsequent steps. We'll assume we're just adding new RUNs to an existing project.
- [ ] Data ends up in
```
/home/server/server2/data/SVR314342810/PROJ13418
/home/server/server2/data/SVR314342810/PROJ13419
```
with a structure of
```
/home/server/server2/data/SVR314342810/PROJ13418/RUN*/CLONE*/results*/
```
- [ ] Each returned WU will contain `results#` directory that looks like this for `(PROJ13418,RUN0,CLONE0,GEN0)`:
```
$ ls -ltr /home/server/server2/data/SVR314342810/PROJ13418/RUN0/CLONE0/results0
total 136
-rw-r--r-- 1 fah-work fah-work  7404 Jul 17 12:00 logfile_01.txt
-rw-r--r-- 1 fah-work fah-work 13851 Jul 17 12:00 science.log
-rw-r--r-- 1 fah-work fah-work 97596 Jul 17 12:00 positions.xtc
-rw-r--r-- 1 fah-work fah-work 13813 Jul 17 12:00 globals.csv
```
The `globals.csv` file contains the `protocol_work` we want to extract and store.

We currently do this using the [`consolidate-work.py`](https://github.com/choderalab/PersesAtFoldingAtHome/blob/add-analysis-script/consolidate-work.py) script to extract two unitless work values (implicitly in units of kT): `forward_work` and `reverse_work`.

We'd also like to archive the `positions.xtc` onto S3 so we can retrieve all the positions associated with individual `(PROJ,RUN,CLONE,GEN)` tuples as desired for further debugging or viewing.

The work values can go into an entry in a table, and then used to compute a free energy estimate for that transformation.

Hannah then uses a [maximum likelihood estimator](https://pubs.acs.org/doi/abs/10.1021/acs.jcim.9b00528) to compute the free energy of that particular ligand (in another table) using the known experimental measured free energies of given ligands and the relative estimated binding free energies among ligands from the transformations table

We also want to extract a snapshot of the ligand B complex form `positions.xtc` (the last snapshot) from each of the result WUs so we can present the chemists with a visual picture of what the protein:ligand interactions might look like.
There's a way to extract a PDB file (a text file) from the last snapshot with a script (using [MDTraj](http://mdtraj.org)) or a command-line tool. These PDB files could be stored as single file objects on S3 and retrieved via a URL when needed.
