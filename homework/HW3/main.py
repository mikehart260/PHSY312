import numpy as np
import matplotlib.pyplot as plt
'''
HIP     Vmag    RA             DE       Plx     pmRA     pmDE   e_Plx   B-V
 It is centered roughly at a right-ascension of 67.6 degrees and
a declination of 16.2 degrees. 
'''
data = np.loadtxt("HW3/Hipparcos_Plx_20_25.dat",skiprows=1)

RA = data[:,2]
DE = data[:,3]


# for line in data:
#     if 69 >= line[2] >= 65 and 14 <= line[3] <= 18:
#         RA.append(line[2])
#         DE.append(line[3])

plt.scatter(RA,DE)
plt.show()


