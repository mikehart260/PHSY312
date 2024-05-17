import numpy as np
import scipy.integrate as sci
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

def spacial(i, j, n, m):
    x = i*dx
    y = j*dx
    return np.sin(n*np.pi*x/L)*np.sin(m*np.pi*y/L)

def frequencies(n, m):
    return np.sqrt((n*np.pi/L)**2 + (m*np.pi/L)**2)

L = 15
t0 = 0
tf = 5
n_points = 50
t_points = 50
n = 1
m = 3

dx = L/n_points # grid spacing 0.1m
dt = (tf - t0)/t_points


U_0 = np.zeros((n_points, n_points))
data = np.zeros((t_points, n_points, n_points))
for t in range(t_points):
    for i in range(1,n_points-1):
        for j in range(1,n_points-1):
            U_0[i][j] = np.cos(frequencies(n,m)*t)*spacial(i,j,n,m)
    data[t] = U_0

####################### PLOT #############################
X, Y = np.meshgrid(np.linspace(0,L,n_points), np.linspace(0,L,n_points))

colortuple = ('y', 'b')
colors = np.empty(X.shape, dtype=str)
for y in range(len(Y)):
    for x in range(len(X)):
        colors[y, x] = colortuple[(x + y) % len(colortuple)]


fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
# ax.plot_surface(X, Y, data[0]) # plot initial surface

# ax.plot_surface(X, Y, data[40], facecolors=colors, linewidth=0) # plot final surface
########################################################################

########################## ANIMATION ###################################
num_frames = t_points
# Function to update the plot for each frame
def update(frame):
    ax.clear()
    ax.set_zlim(-1, 1)  # Adjust Z limit if necessary
    ax.set_title(f'Time Frame: {frame + 1}/{num_frames}')
    surf = ax.plot_surface(X, Y, data[frame], cmap='viridis')
    return surf,

# Create animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=10)
###################################################################

plt.show()
