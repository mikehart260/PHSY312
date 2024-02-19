'''
@file main.py
Michael Hart
Main file for HW2.
'''
# imports
import numpy as np
import os
import matplotlib.pyplot as plt

# Load in files that begin with uk
directory = os.listdir('StellarSpectraFiles')
for filename in directory:
    wavelength = []
    intensity = []
    if filename[:2] == "uk":
        full_filename = "StellarSpectraFiles/" + filename
        filename = filename.split('.')
        data = np.loadtxt(full_filename,skiprows=3,usecols=[0,1])
        for line in data:
            if 6650 >= int(line[0]) >= 6500:
                wavelength.append(int(line[0]))
                intensity.append(float(line[1]))
        plt.plot(wavelength,intensity,label=filename[0][2:])         

plt.xlabel("Wavelength")
plt.ylabel("Intesity")
plt.legend()
plt.show()



