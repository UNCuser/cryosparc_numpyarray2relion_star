
# WAIT... READ THIS..

# Usage: python3 <script name> <cs file> <subscript> <x-normalization factor> <y-normalization factor>
# Example for K3: python3 py3XYnumpy2star.py P954_J83_particles_exported.cs manualpick 5760 4092 
# 
# CAUTION: Sanity checks are not in place -- if the program is run without the args above, undesirable things might happen -- inf loop or crash etc
import os
import re
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

particle_locs = {}
for j in range(len(particles)):
	particle_locs[str(particles[j])]=[]

for j in range(len(particles)):
	particle_locs[str(particles[j])].append([X[j]*float(x_norm), Y[j]*float(y_norm)])

stdout_ref = sys.stdout
for parti in particles:
	noSlashes = parti.split(b'/')
	noUndies = noSlashes[-1].split(b'_')
	date = repr(str(noUndies[1])[2:-1])
	date = re.sub("[']", '', date)
	nav_item = repr(str(noUndies[2])[2:-1])
	nav_item = re.sub("[']", '', nav_item)
	shot_num = repr(str(noUndies[3])[2:-1])
	shot_num = re.sub("[']", '', shot_num)

	filename = date + '_' + nav_item + '_' + shot_num + '_' + subscript + out_ext
	
	

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
