import math

g = 9.8

dino_hash = {}
dino_file = open("dino_2.txt","r")
for ln in dino_file:
    dino_array = ln.strip().split(',')
    if(dino_array[2] == 'bipedal'):
        dino_hash[dino_array[0]] = float(dino_array[1])

dino_file.close()

dino_file = open("dino_1.txt", 'r')
for ln in dino_file:
    dino_array = ln.strip().split(',')
    if(dino_array[0] in dino_hash.keys()):
        print("Checking for " + dino_array[0])
        speed = ((dino_hash[dino_array[0]]/float(dino_array[1])) - 1) * math.sqrt(float(dino_array[1]) * g)
        print("Speed for " + dino_array[0] + ": " + str(speed))



print(dino_hash)