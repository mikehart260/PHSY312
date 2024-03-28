# Q7.5.2, P7.5.4,
# P7.7.3*

#Q7.5.2

import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('/Users/michaelhart/repos/PHSY312/pair/week_09/birthday-data.csv',skip_header=1,delimiter=',',dtype=int)
clean = []
for line in data:
    if line[2] > 1000:
        clean.append(line)

clean = np.array(clean)


month = clean[:,0]
day = clean[:,1]
births = clean[:,2]

heatmap = np.empty((12,31))
heatmap[:] = np.nan
sum = np.sum(births)
print(len(births))
for month, day, births in clean:
    heatmap[month-1,day-1] = births/sum *100


fig = plt.figure()
ax = fig.add_subplot()
im = ax.imshow(heatmap)
ax.set_yticks(range(12))
ax.set_yticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', "Jun", 'Jul', 'Aug', 'Sep', 'Oct','Nov', 'Dec'])

days = np.array(range(0,31,2))
ax.set_xticks(days)
ax.set_xlabel("day of the month")

cbar = fig.colorbar(ax=ax, mappable=im, orientation='horizontal') 
cbar.set_label('Probabilty to be born on a day')

plt.show()

