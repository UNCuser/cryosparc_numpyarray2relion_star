# cryosparc_numpyarray2relion_star
The project will take a standard exported particles cryosparc_file.cs numpy array out. 
It will convert the X and Ys to manual_pick.star files for simple conversion of cryoEM particle X and Y picks into relion.
Output of this script can be dumped into a relion manualpick job folder and particles extracted to start a clean processing tree with your favorite particles from cryosparc.

To use: (1) Export your favorate particle job from cryosparc (2) cd to the P(roject)/jobs/export/P(roject)J(ob)/P(roject)J(ob)-particles
(3) run as listed below (4) move manualpick.star files to appropriate relion manual pick directory 

#Note: If you want to use motion corrected files from cryosparc instead of from relion, be sure to match manualpick files to also include the cryosparc prefix if present or rename motioncorrected.mrc files to omit CSpresfix.  

To use run program: 
python script_name   cs_file    subscript  Xnormalization_factor   Ynormalization_factor

Example for K3: python XYnumpy2star.py P54_J83_particles_exported.cs manualpick 5760 4092
Example for K2: python XYnumpy2star.py P999_J999_particles_exported.cs manualpick 3710 3838

#Note: if XYnumpy2star.py will not run try JVP modified python3 version py3XYnumpy2star.py
