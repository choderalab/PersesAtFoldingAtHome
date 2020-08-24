load EN300-26624333-charged-boronic_esterbackwards.pdb 
load EN300-365771-charged-boronic_esterbackwards.pdb 
load EN300-316592-charged-boronic_esterbackwards.pdb 
load EN300-298506-charged-boronic_esterbackwards.pdb 
load EN300-1086686-charged-boronic_esterbackwards.pdb 
load EN300-106778-charged-boronic_esterbackwards.pdb 
load EN300-303608-charged-boronic_esterbackwards.pdb 
load EN300-129678-charged-boronic_esterbackwards.pdb 
load EN300-1425849-charged-boronic_esterbackwards.pdb 
load EN300-364488-charged-boronic_esterbackwards.pdb 
load EN300-148395-charged-boronic_esterbackwards.pdb 
load EN300-122703-charged-boronic_esterbackwards.pdb 
load EN300-1704613-charged-boronic_esterbackwards.pdb 
load EN300-218797-charged-boronic_esterbackwards.pdb 
extra_fit resi [187-192,164-168,140-145], EN300-218797-charged-boronic_esterbackwards, super, object=aln_super 
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
