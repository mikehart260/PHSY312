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
        full_filename = "StellarSpectraFiles" +os.sep + filename
        filename = filename.split('.')
        data = np.loadtxt(full_filename,skiprows=3,usecols=[0,1])
        sum = 0
        count = 0
        for line in data:
            if 6600 <= int(line[0]) <= 6650:
                # calculates average intensity for 50 nm before range of plot
                sum += float(line[1]) 
                count += 1
            if 6500 <= int(line[0]) <= 6650: 
                wavelength.append(int(line[0])*0.1) # convert to nm
                intensity.append(float(line[1]))
        plt.plot(wavelength,np.array(intensity)/(sum/count),label=f"Type {filename[0][2]}")

plt.xlabel("Wavelength (nm)")
plt.ylabel("Intesity")
plt.legend()
plt.show()