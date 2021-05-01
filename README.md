# cryosparc_numpyarray2relion_star
The project will take a standard exported cryosparc_file.cs numpy array out. 
It will convert the X and Ys to manual_pick.star files for simple conversion of cryoEM particle X and Y picks into relion.

To use run program: 
"python script_name cs_file subscript x-normalization_factor y-normalization_factor

Example for K3: python NUMPY_Whisperer.py P54_J83_particles_exported.cs manualpick 5760 409
  
