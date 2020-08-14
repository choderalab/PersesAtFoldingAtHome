load EN300-365771-neutral-boronic_esterbackwards.pdb 
load EN300-316592-neutral-boronic_esterbackwards.pdb 
load EN300-1722014-neutral-boronic_esterbackwards.pdb 
load EN300-364488-neutral-boronic_esterbackwards.pdb 
load EN300-26624333-neutral-boronic_esterbackwards.pdb 
load EN300-1704613-neutral-boronic_esterbackwards.pdb 
load EN300-1086686-neutral-boronic_esterbackwards.pdb 
load EN300-299518-neutral-boronic_esterbackwards.pdb 
load EN300-391783-neutral-boronic_esterbackwards.pdb 
load EN300-129678-neutral-boronic_esterbackwards.pdb 
load EN300-106778-neutral-boronic_esterbackwards.pdb 
load EN300-1425849-neutral-boronic_esterbackwards.pdb 
load EN300-705961-neutral-boronic_esterbackwards.pdb 
load EN300-298506-neutral-boronic_esterbackwards.pdb 
load EN300-363385-neutral-boronic_esterbackwards.pdb 
load EN300-6489774-neutral-boronic_esterbackwards.pdb 
load EN300-148395-neutral-boronic_esterbackwards.pdb 
load EN300-359542-neutral-boronic_esterbackwards.pdb 
load EN300-246322-neutral-boronic_esterbackwards.pdb 
load EN300-363413-neutral-boronic_esterbackwards.pdb 
load EN300-122703-neutral-boronic_esterbackwards.pdb 
load EN300-172191-neutral-boronic_esterbackwards.pdb 
extra_fit resi [187-192,164-168,140-145], EN300-172191-neutral-boronic_esterbackwards, super, object=aln_super 
set cartoon_color, gray
hide spheres
hide (h. and (e. c extend 1))
set cartoon_transparency, 0.5 
sele ligands, resn MOL 
sele GLU, resid 166 
sele HIS, resid 41 
show licorice, GLU 
show licorice, HIS 
orient ligands 
delete aln_super 
save ligands.sdf, ligands
bg_color white