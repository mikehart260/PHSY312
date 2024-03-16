import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial as poly
import statsmodels.api as sm
# 'HIP', 'Vmag', 'RA', 'DE', 'Plx', 'pmRA', 'pmDE', 'e_Plx', 'BV'
data = np.genfromtxt("/Users/michaelhart/repos/PHSY312/homework/HW5/Hipparcos_Plx_20_25-1.dat", names = True)


def temp(BV):
    return 4600*((1/(.92*BV+.7))+(1/(0.92*BV+0.62)))

O, B, A, F, G, K, M = '#0000f8','#0000FF', '#babaf8', '#FFFFFF', '#FDB813' , '#FFA500' , '#ff0000'

color= []

for star in data["BV"]:
    temps = temp(star)
    if 30000 < temps <= 60000:
        color.append(O)
    elif 10000 < temps <= 30000:
        color.append(B)
    elif 7500 < temps <= 10000:
        color.append(A)
    elif 6000 < temps <= 7500:
        color.append(F)
    elif 5000 < temps <= 6000:
        color.append(G)
    elif 3500 < temps <= 5000:
        color.append(K)
    else:
        color.append(M)

fig, ax = plt.subplots()

def fit(x,b,c,d):
    return  b*x**2 + c*x + d

## smoothing ## 
lowess = sm.nonparametric.lowess(data["Vmag"], data["BV"])
lowess_x = list(zip(*lowess))[0]
lowess_y = list(zip(*lowess))[1]

plt.plot(lowess_x, lowess_y, color='violet', label='LOWESS')

ax.scatter(data["BV"],data["Vmag"],s=0.7,c=color)
ax.annotate("Main Sequence",(2.0,7.6),(1.2,10.3))
ax.set_facecolor('k')
ax.set_ylabel("Absolute Magnitude")
ax.set_xlabel("Color B-V")
ax.invert_yaxis()
plt.show()