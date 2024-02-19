# @file main.py
# Michael Hart
# mhart1
# file that accepts a file and elevation and returns the distance with the closest elevation.
from numpy import loadtxt as ld

def get_file():
    return input("filename: ")

def get_elevation():
    return input("Elevation: ")

def validate_file(file):
    # checks file exists.
    try: data = ld(file,skiprows=1,dtype=str,delimiter=',')
    except: 
        print("File not found.")
        return False
    else: return True

def validate_elevation(elevation):
    # checks elevation is float.
    try: float(elevation)
    except ValueError: 
        print("Elevation should be float.")
        return False
    else: return True

def find_distance(file, desired_elevation):
    data = ld(file,skiprows=1,dtype=str,delimiter=',')
    diff = 1000
    for line in data:
        if abs(desired_elevation - float(line[1])) < diff:
            diff = abs(desired_elevation - float(line[1]))
            elevation = line[1]
            distance = line[0]
    return (float(distance), float(elevation))

# value validation.
file = get_file()
while (not validate_file(file)):
    file = get_file()
desired_elevation = get_elevation()
while (not validate_elevation(desired_elevation)):
    desired_elevation = get_elevation()

distance , elevation = find_distance(file,float(desired_elevation))
print("Distance : {0:.3f} m".format(distance))