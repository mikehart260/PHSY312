import numpy as np
import matplotlib.pyplot as plt
'''
HIP     Vmag    RA             DE       Plx     pmRA     pmDE   e_Plx   B-V
 It is centered roughly at a right-ascension of 67.6 degrees and
a declination of 16.2 degrees. 
'''
data = np.loadtxt("Hipparcos_Plx_20_25.dat",skiprows=1)

# RA = data[:,2]
# DE = data[:,3]

'''
For stars nearby the average positon, find their average distance from it. 
'''
plt.close('all')
RA = []
DE = []
std_hist = []
avg_hist = []
for i in range(200): 
    rand = np.random.randn(1)
    avg_RA = 0
    avg_DE = 0
    count = 0
    RA = []
    DE = []
    for line in data:
        if (50.0+rand <= line[2] <= 82.0+rand and 6.0+rand <= line[3] <= 26.0+rand):
            RA.append(line[2])
            DE.append(line[3])
            avg_RA += line[2]
            avg_DE += line[3]
            count+= 1
    avg_RA /= count
    avg_DE /= count

    distances = []
    for i in range(len(RA)):
        x = RA[i]
        y = DE[i]
        distances.append( np.sqrt((avg_RA-x)**2 + (avg_DE - y)**2) )
    distances = np.array(distances) 

    avg_distance_from_center = np.average(distances)
    std_distances = np.std(distances)
    #print(f"Average Distance: {avg_distance_from_center}, STDEV: {std_distances}")
    std_hist.append(std_distances)
    avg_hist.append(avg_distance_from_center)

plt.hist(avg_hist)
plt.title("Average distance")
plt.show()
plt.hist(std_hist)
plt.title("STDEV")
plt.show()


'''
Average distance was 5.618 with a STDEV of 4.27 so the majority of the stars in that
region were from 1-9.88 away from the 

'''

# plt.scatter(RA,DE)
# plt.scatter(67.6, 16.2)
# plt.show()