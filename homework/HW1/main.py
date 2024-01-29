from numpy import loadtxt as ld
def get_file():
    return input("filename: ")
def get_elevation():
    return input("Elevation: ")
def validate_file(file):
    try: data = ld(file,skiprows=1,dtype=str,delimiter=',')
    except: print("File not found.")
    else: return True
    return False
def validate_elevation(elevation):
    try: float(elevation)
    except ValueError: print("Elevation should be float.")
    else: return True
    return False

def find_distance(file, desired_elevation):

    data = ld(file,skiprows=1,dtype=str,delimiter=',')
    diff = 1000
    idx = 0
    # distance = line[0]
    # elevation = line[1]
    # idx = data[line]
    for line in data:
        if abs(desired_elevation - float(line[1])) < diff:
            diff = abs(desired_elevation - float(line[1]))
            elevation = line[1]
            distance = line[0]
        idx+=1
    return (float(distance), float(elevation))

file = get_file()
while (not validate_file(file)):
    file = get_file()
desired_elevation = get_elevation()
while (not validate_elevation(desired_elevation)):
    desired_elevation = get_elevation()

distance , elevation = find_distance(file,float(desired_elevation))
print("Distance : {0:.3f} m, Elevation : {1:.3f} m".format(distance, elevation))