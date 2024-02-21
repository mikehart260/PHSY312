'''
@file main.py
Michael Hart
Main file for HW2.
'''
# imports
import numpy as np
import os
import matplotlib.pyplot as plt
fig = plt.figure()
# Load in files that begin with uk
directory = os.listdir('StellarSpectraFiles')
star_types = []
for filename in directory:
    wavelength = []
    intensity = []
    if filename[:2] == "uk":
        full_filename = "StellarSpectraFiles" +os.sep + filename
        filename = filename.split('.')
        star_types.append(f"Type {(filename[0][2]).upper()}")
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
        plt.plot(wavelength,np.array(intensity)/(sum/count),label=f"Type {(filename[0][2]).upper()}")

# Stack overflow code https://stackoverflow.com/questions/50791422/plotting-sequences-with-same-label-and-color-in-python
ax = fig.gca() # get current axis
for i, p in enumerate(ax.get_lines()):
    if p.get_label() in star_types[:i]:
        idx = star_types.index(p.get_label())       # find ist index
        p.set_c(ax.get_lines()[idx].get_c())   # set color
        p.set_label('_' + p.get_label()) 

# my code to potentially sort the legend. 
# lines = []
# for i, p in enumerate(ax.get_lines()):
#     print("i: ",i," p: ",p)
#     if len(lines) == 0:
#         lines.append(ax.get_lines()[i])
#     else:
#         for line in lines:
#             if p.get_label()[-1] < line.get_label()[-1]:
#                 idx = lines.index(line)
#                 lines.insert(idx,ax.get_lines()[i])
# print(lines)

plt.xlabel("Wavelength (nm)")
plt.ylabel("Intesity")
plt.legend()
plt.show()