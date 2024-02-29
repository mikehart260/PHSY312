'''
@file main.py
Michael Hart
Main file for HW2.
'''
# imports
import numpy as np
import os
import matplotlib.pyplot as plt

stellar_dict = {}
# Load in files that begin with uk
directory = os.listdir('StellarSpectraFiles')
for filename in directory:
    if filename[:2] == "uk":
        full_filename = "StellarSpectraFiles" + os.sep + filename
        star_type = (filename.split('.'))[0][2]
        data = np.loadtxt(full_filename,skiprows=3,usecols=[0,1])
        sum = 0
        count = 0
        if (star_type not in stellar_dict.keys()):
            stellar_dict[star_type] = np.array([],[]) # {"A": [<wavelength>],[<intensity>]}
        for line in data:
            if 6500 <= int(line[0]) <= 6650: 
                wavelength.append(int(line[0])*0.1) # convert to nm
                intensity.append(float(line[1]))
            elif 6600 <= int(line[0]) <= 6650:
                # calculates average intensity for 50 nm before range of plot
                sum += float(line[1]) 
                count += 1
            