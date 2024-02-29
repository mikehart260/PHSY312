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

directions = []

for line in data:
         if (50.0 <= line[2] <= 82.0 and 6.0 <= line[3] <= 26.0):
             dir = vector_dir(1/line[5],1/line[6])
             directions.append(dir) 
            
plt.arrow(line[2],line[3],1/line[5],1/line[6],width=1,head_width = 1)
                
directions = np.array(directions)

print(mode(np.round(directions))) # MODE was 80
'''

'''
    PLOTTING STARS IN THE CLUSTER TO INCLUDE VS NOT INCLUDE.
    ALSO CALCULATE AVERAGE AND STDEV OF THE VELOCITIES.

    RESULTS: 
'''

dirs = []
count = 0
for line in data:
    RA = line[2]
    DEC = line[3]
    if(46.1 <= RA <= 86.1 and 0.0 <= DEC <= 32.0):
        dir = vector_dir(1/line[5],1/line[6])
        if (-90.207 < dir < -61.803): # Two standard deviations
            print(dir)
            plt.arrow(RA,DEC,1/line[5],1/line[6],width=1,head_width = 1)
            dirs.append(dir)
        else:
            plt.arrow(RA,DEC,1/line[5],1/line[6],width=1,head_width = 1, color='red')            


print(f"Number of stars included: {len(dirs)}")
print(np.average(dirs))
print(np.std(dirs))

''' -71.2626 -> -80.7486 is one stdev
    -66.537  -> -85.473 is two stdev
'''


plt.xlabel("East-West")
plt.ylabel("North-South")
plt.title("Cluster")
plt.show()

plt.figure()
plt.hist(dirs)

plt.show()

