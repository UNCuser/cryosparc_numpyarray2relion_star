# cryosparc_numpyarray2relion_star
The project will take a standard exported particles cryosparc_file.cs numpy array out. 
It will convert the X and Ys to manual_pick.star files for simple conversion of cryoEM particle X and Y picks into relion.
Output of this script can be dumped into the appropriate relion manualpick job sub-folder and particles extracted to start a clean processing tree with your favorite particles from cryosparc.

## Download CLI
>git clone https://github.com/UNCuser/cryosparc_numpyarray2relion_star

## To use:
- **(1)** Export your favorate particle job from cryosparc 
- **(2)** cd to the P(roject)/jobs/export/P(roject)J(ob)/P(roject)J(ob)-particles
- **(3)** run as listed below 
- **(4)** move manualpick.star files to appropriate relion manual pick directory 

_Note1: If you want to use motion corrected files from cryosparc instead of from relion, be sure to match manualpick files to also include the cryosparc prefix if present or rename motioncorrected.mrc files to omit CSpresfix, as shown below._  
>Example: for file in \*.mrc\; do ln -s $file \${file#*_} ; done

_Note2: You may need to flip Y (unhash Y-flip & hash noflip) if using relion motion corrected files._
> add hash to line 36 and remove hash on line 38 to run w/Y flip

## To run program:
**python script_name   cs_file    subscript  Xnormalization_factor   Ynormalization_factor**

>Example for K3: python XYnumpy2star.py P54_J83_particles_exported.cs manualpick 5760 4092
>
>Example for K2: python XYnumpy2star.py P999_J999_particles_exported.cs manualpick 3710 3838

_Note: if XYnumpy2star.py will not run try JVP modified python3 version py3XYnumpy2star.py You may have to make a python3 environment with numpy for this._
> Example for K3: python3 py3XYnumpy2star.py P54_J83_particles_exported.cs manualpick 5760 4092
