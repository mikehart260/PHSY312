import numpy as np
import matplotlib.pyplot as plt
wl = np.linspace(0,5000,100)
print(wl)

fig, ax = plt.subplots()
ax.scatter(wl,wl)

ax.invert_xaxis()
ax.set_xlim(4000,0)

plt.show()

