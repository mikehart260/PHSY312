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

# directions = []

# for line in data:
#         if (50.0 <= line[2] <= 82.0 and 6.0 <= line[3] <= 26.0):
#             dir = vector_dir(1/line[5],1/line[6])
#             directions.append(dir) 
            
# plt.arrow(line[2],line[3],1/line[5],1/line[6],width=1,head_width = 1)
                
# directions = np.array(directions)

# print(mode(np.round(directions))) # MODE was 80

'''
    Now lets calculate the residuals of the stars directions. 
'''
DRIFT = -80
dirs = []
for line in data:
    if (50.0 <= line[2] <= 82.0 and 6.0 <= line[3] <= 26.0):
        dir = vector_dir(1/line[5],1/line[6])
        if (-95 < dir < -67):
            print(dir)
            plt.arrow(line[2],line[3],1/line[5],1/line[6],width=1,head_width = 1)
            dirs.append(dir)


print(len(dirs))
print(np.average(dirs))
print(np.std(dirs))

''' -71.2626 -> -80.7486 is one stdev'''


plt.xlabel("East-West")
plt.ylabel("North-South")
plt.title("Most common direction is -80 degrees.")
plt.show()

plt.figure()
plt.hist(dirs)
plt.legend()
plt.show()

