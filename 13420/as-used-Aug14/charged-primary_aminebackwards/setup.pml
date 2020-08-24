load EN300-20814457-charged-primary_aminebackwards.pdb 
load EN300-59553-charged-primary_aminebackwards.pdb 
load EN300-6734624-charged-primary_aminebackwards.pdb 
load EN300-60314-charged-primary_aminebackwards.pdb 
load EN300-2009339-charged-primary_aminebackwards.pdb 
load EN300-6486612-charged-primary_aminebackwards.pdb 
load EN300-124496-charged-primary_aminebackwards.pdb 
load EN300-393345-charged-primary_aminebackwards.pdb 
load EN300-6497035-charged-primary_aminebackwards.pdb 
load EN300-1708634-charged-primary_aminebackwards.pdb 
load EN300-136221-charged-primary_aminebackwards.pdb 
load EN300-212829-charged-primary_aminebackwards.pdb 
load EN300-7445610-charged-primary_aminebackwards.pdb 
load EN300-703002-charged-primary_aminebackwards.pdb 
load EN300-384108-charged-primary_aminebackwards.pdb 
load EN300-312320-charged-primary_aminebackwards.pdb 
load EN300-75221-charged-primary_aminebackwards.pdb 
load EN300-59896-charged-primary_aminebackwards.pdb 
load EN300-262200-charged-primary_aminebackwards.pdb 
load EN300-7430703-charged-primary_aminebackwards.pdb 
load EN300-262201-charged-primary_aminebackwards.pdb 
load EN300-131018-charged-primary_aminebackwards.pdb 
load EN300-352243-charged-primary_aminebackwards.pdb 
load EN300-321398-charged-primary_aminebackwards.pdb 
load EN300-6736658-charged-primary_aminebackwards.pdb 
load EN300-344955-charged-primary_aminebackwards.pdb 
load EN300-363585-charged-primary_aminebackwards.pdb 
load EN300-89718-charged-primary_aminebackwards.pdb 
load EN300-378161-charged-primary_aminebackwards.pdb 
load EN300-26620085-charged-primary_aminebackwards.pdb 
load EN300-52283-charged-primary_aminebackwards.pdb 
load EN300-1074309-charged-primary_aminebackwards.pdb 
load EN300-26667249-charged-primary_aminebackwards.pdb 
load EN300-650549-charged-primary_aminebackwards.pdb 
load EN300-1700325-charged-primary_aminebackwards.pdb 
load EN300-189763-charged-primary_aminebackwards.pdb 
extra_fit resi [187-192,164-168,140-145], EN300-189763-charged-primary_aminebackwards, super, object=aln_super 
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
