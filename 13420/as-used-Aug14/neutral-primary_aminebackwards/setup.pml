load EN300-60314-neutral-primary_aminebackwards.pdb 
load EN300-59553-neutral-primary_aminebackwards.pdb 
load EN300-6734624-neutral-primary_aminebackwards.pdb 
load EN300-1723947-neutral-primary_aminebackwards.pdb 
load EN300-7434265-neutral-primary_aminebackwards.pdb 
load EN300-342028-neutral-primary_aminebackwards.pdb 
load EN300-2515954-neutral-primary_aminebackwards.pdb 
load EN300-6497035-neutral-primary_aminebackwards.pdb 
load EN300-26620085-neutral-primary_aminebackwards.pdb 
load EN300-1692178-neutral-primary_aminebackwards.pdb 
load EN300-295395-neutral-primary_aminebackwards.pdb 
load EN300-7429945-neutral-primary_aminebackwards.pdb 
load EN300-352243-neutral-primary_aminebackwards.pdb 
load EN300-315164-neutral-primary_aminebackwards.pdb 
load EN300-59896-neutral-primary_aminebackwards.pdb 
load EN300-131018-neutral-primary_aminebackwards.pdb 
load EN300-650549-neutral-primary_aminebackwards.pdb 
load EN300-153078-neutral-primary_aminebackwards.pdb 
load EN300-7430703-neutral-primary_aminebackwards.pdb 
load EN300-6512862-neutral-primary_aminebackwards.pdb 
load EN300-365363-neutral-primary_aminebackwards.pdb 
load EN300-201994-neutral-primary_aminebackwards.pdb 
load EN300-75221-neutral-primary_aminebackwards.pdb 
load EN300-7434894-neutral-primary_aminebackwards.pdb 
load EN300-344955-neutral-primary_aminebackwards.pdb 
load EN300-1272614-neutral-primary_aminebackwards.pdb 
load EN300-1604839-neutral-primary_aminebackwards.pdb 
load EN300-6478226-neutral-primary_aminebackwards.pdb 
load EN300-26974864-neutral-primary_aminebackwards.pdb 
load EN300-212829-neutral-primary_aminebackwards.pdb 
load EN300-115150-neutral-primary_aminebackwards.pdb 
extra_fit resi [187-192,164-168,140-145], EN300-115150-neutral-primary_aminebackwards, super, object=aln_super 
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
