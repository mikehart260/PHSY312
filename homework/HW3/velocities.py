import numpy as np
import matplotlib.pyplot as plt
'''
HIP     Vmag    RA             DE       Plx     pmRA     pmDE   e_Plx   B-V
 It is centered roughly at a right-ascension of 67.6 degrees and
a declination of 16.2 degrees. 

1/pmRA 1/pmDE
'''
data = np.loadtxt("Hipparcos_Plx_20_25.dat",skiprows=1)
'''
Here we calculated the most common direction from this patch of sky to be -80 degress.
'''

def vector_dir( v_RA , v_DE):
     theta = np.arctan2(v_DE,v_RA)
     return np.degrees(theta)

def mode(arr):
    unique, counts = np.unique(arr, return_counts=True)
    max_count_index = np.argmax(counts)
    return unique[max_count_index]

'''
    CODE TO FIND THE MOST COMMON VELOCITY OF THE CLUSTER.
    # Avg Pos and std dev RA DE -> 66.1 0.7  16.5 .7
'''
directions = []

for line in data:
         if (64.7 <= line[2] <= 67.5 and 15.1 <= line[3] <= 17.9):
             dir = vector_dir(1/line[5],1/line[6])
             directions.append(dir)
             #plt.arrow(line[2],line[3],1/line[5],1/line[6],width=1,head_width = 1)
                
directions = np.array(directions)

# print(np.average(directions))
# print(np.std(directions))
# print(mode(np.round(directions))) # MODE was 80
# print(len(directions))
# plt.show()

'''
    PLOTTING STARS IN THE CLUSTER TO INCLUDE VS NOT INCLUDE.
    ALSO CALCULATE AVERAGE AND STDEV OF THE VELOCITIES.

    RESULTS: 
'''
v_std = 2.3
dirs = []
count = 0
# for i in range(100):
    
    
#     print(len(dirs))
#     dirs = []
#     rand = np.random.randn(1)
stars = []
for line in data:
    RA = line[2]
    DEC = line[3]
    if(50 <= RA <= 80 and 5 <= DEC <= 30):
        dir = vector_dir(1/line[5],1/line[6])
        if (-82.4-(v_std) < dir < -68.6+(v_std)): # Two standard deviations of direction
            #print(dir)
            plt.arrow(RA,DEC,1/line[5],1/line[6],width=1,head_width = 1)
            dirs.append(dir)
            stars.append(line[0])
        else:
            plt.arrow(RA,DEC,1/line[5],1/line[6],width=1,head_width = 1, color='red')

print(stars)
print(f"Number of stars included: {len(dirs)}")
print(np.average(dirs))
print(np.std(dirs))

plt.arrow([], [],[],[], color='blue', label='Included in Cluster')
plt.arrow([], [],[],[], color='red', label='Not Included in Cluster')
plt.xlabel("Right Acension")
plt.ylabel("Declination")
plt.title("Cluster")
plt.legend()
plt.show()

# plt.figure()
# plt.hist(dirs)

# plt.show()

