# WAIT... READ THIS..

# Usage: python <script name> <cs file> <subscript> <x-normalization factor> <y-normalization factor>
# Example for K3: python XYnumpy2star.py P954_J83_particles_exported.cs manualpick 5760 4092 
# 
# CAUTION: Sanity checks are not in place -- if the program is run without the args above, undesirable things might happen -- inf loop or crash etc

import numpy as np
import sys

cs_file = sys.argv[1]
cs = np.load(cs_file)

# since your project names might be different in the future, I'm leaving the subscript as a variable.
# This is the part that follows the date and the two numbers in the long identifier. subscript is appended to
# the string generated from the long identifier to generate the output file name.
subscript = sys.argv[2]
# vars from the shell script are converted to variables here -- read from command line input to this python script
x_norm = sys.argv[3]
y_norm = sys.argv[4]

out_ext = ".star"

#potential variables
particles = cs['blob/path']
X = cs['location/center_x_frac']
Y = cs['location/center_y_frac']
#y flip
#Y = 1 - cs['location/center_y_frac']

particle_locs = {}
for j in range(len(particles)):
	particle_locs[str(particles[j])]=[]

for j in range(len(particles)):
	particle_locs[str(particles[j])].append([X[j]*float(x_norm), Y[j]*float(y_norm)])
	
stdout_ref = sys.stdout
for parti in particles:
	noSlashes = parti.split("/")
	noUndies = noSlashes[-1].split("_")
	filename = str(noUndies[1])+"_"+str(noUndies[2])+"_"+str(noUndies[3])+"_"+str(subscript)+str(out_ext)
#add head
	with open(filename,'w') as f:
		sys.stdout = f
		print("data_")
		print("")
		print("loop_")
		print("_rlnCoordinateX #1")
		print("_rlnCoordinateY #2")
		print("")
		for x in range(len(particle_locs[str(parti)])):
			print(' '.join(map(str, particle_locs[str(parti)][x])))
sys.stdout = stdout_ref
