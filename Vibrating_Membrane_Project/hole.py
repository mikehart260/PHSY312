import numpy as np
import scipy.integrate as sci
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

L = 1
t0 = 0
tf = 100
n_points = 20
t_points = 1000

dx = L/n_points # grid spacing
dt = (tf - t0)/t_points

wavespeed_m_s = 0.15 # wavespeed

# constant wavespeed grid
C = wavespeed_m_s*np.ones((n_points,n_points))

U_0 = np.ones((n_points, n_points))

# Add a "hole" in the initial conditions
center = 5
U_0[center][center+1] = 0
U_0[center+1][center]= 0
U_0[center+1][center+1] =0
U_0[center-1][center-1] = 0
U_0[center][center] = 0
U_0[center-1][center] = 0
U_0[center][center-1] = 0
U_0[center-1][center+1] = 0
U_0[center+1][center-1] = 0

# initialize U for n+1 and n-1
U_prev = U_0
U_1 = np.zeros_like(U_0)
data = np.zeros((t_points, n_points, n_points))

######## CENTRAL DIFFERENCE BASED ON SQUARE BOUNDARY CONDITIONS W/ HOLE ##############
for t in range(t_points):
    for j in range(1,n_points-1):
        for k in range(1,n_points-1):
            if ((j==center and k ==center) or (j==center-1 and k==center-1) or (j==center and k==center-1) or (j==center-1 and k==center) or 
                (j==center and k==center+1) or (j==center+1 and k==center) or (j==center-1 and k==center+1) or (j==center+1 and k==center-1) or (j==center+1 and k==center+1)):
                U_1[j][k] = 0
            else:    
                U_1[j][k] = (dt/dx)**2 * (C[j][k])**2 * (U_0[j+1][k] - 4*U_0[j][k] + 
                        U_0[j-1][k] + U_0[j][k+1] + U_0[j][k-1]) + 2*U_0[j][k] - U_prev[j][k]
    data[t] = U_1
    U_prev = U_0.copy() 
    U_0 = U_1.copy() 
##############################################################################

####################### PLOT #############################
X, Y = np.meshgrid(np.linspace(0,L,n_points), np.linspace(0,L,n_points))

colortuple = ('y', 'b')
colors = np.empty(X.shape, dtype=str)
for y in range(len(Y)):
    for x in range(len(X)):
        colors[y, x] = colortuple[(x + y) % len(colortuple)]

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

########################## ANIMATION ###################################
num_frames = t_points

def update(frame): # Function to update the plot for each frame
    ax.clear()
    ax.set_zlim(-2, 2)  # Adjust Z limit if necessary
    ax.set_title(f'Hole at {center}\nTime Frame: {frame + 1}/{num_frames}')
    surf = ax.plot_surface(X, Y, data[frame], cmap='viridis')
    return surf,

# Create animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=10)
###################################################################
plt.title(f"Hole at {center}")
plt.show()