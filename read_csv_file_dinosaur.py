# You will be supplied with two data files in CSV format. The first file contains
# statistics about various dinosaurs. The second file contains additional data.
# Given the following formula,
#
# speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
# Where g = 9.8 m/s^2 (gravitational constant)

# Write a program to read in the data files from disk, it must then print the names
# of only the bipedal dinosaurs from fastest to slowest. Do not print any other information.

# The solution here is to read the file which contains the information about number of legs (dino-2.txt). Filter on
# bipedal dinosaurs and then add the dino name and leg length in a hash/dictionary
# Next open the second file (dino_1.txt). Iterate line by line and match dinos by name to the keys in the earlier
# created hash. Extract stride length and then calculate and print speed

import math
# Gravitational constant (9.8 m/s2)
g = 9.8
#hash for storing dino name and leg length
dino_hash = {}

# Open file containing dino name, number of legs
dino_file = open("dino_2.txt","r")
for ln in dino_file:
    # Taking each row, stripping leading and trailing spaces, and splitting based on comma
    dino_array = ln.strip().split(',')
    if(dino_array[2] == 'bipedal'):
        # Add bipedal dinos to hash
        dino_hash[dino_array[0]] = float(dino_array[1])

dino_file.close()

# Open file containing dino stride length
dino_file = open("dino_1.txt", 'r')
for ln in dino_file:
    dino_array = ln.strip().split(',')
    # Only need to consider dinos which are bipedal (i.e. contained in hash)
    if(dino_array[0] in dino_hash.keys()):
        speed = ((dino_hash[dino_array[0]]/float(dino_array[1])) - 1) * math.sqrt(float(dino_array[1]) * g)
        print("Speed for " + dino_array[0] + ": " + str(speed))

dino_file.close()