import numpy as np
import scipy.integrate as sci
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
# project code due 4/24

L = 1
t0 = 0
tf = 10
n_points = 20
t_points = 100

dx = L/n_points # grid spacing
dt = (tf - t0)/t_points

wavespeed_m_s = 0.1 # wavespeed

# constant wavespeed grid
C = wavespeed_m_s*np.ones((n_points,n_points))

####### SET UP INITIAL STATE WITH SQUARE BOUNDARY CONDITIONS ######
# U_0 = np.ones((n_points, n_points))

# for j in range(n_points):
#     for k in range(n_points):
#         if j == n_points-1 or k == n_points-1 or j == 0 or k == 0:
#              U_0[j][k] = 0
##################################################################

####### SET UP DELTA FUNCTION INITIAL STATE WITH SQUARE BOUNDARY CONDITIONS ######
U_0 = np.zeros((n_points, n_points))
x_coordinate = 5 # x coordinate for delta function in terms of L
y_coordinate = 5 # y coordinate for delta function in terms of L
delta_magnitude = 2

U_0[x_coordinate][y_coordinate] = -delta_magnitude

# initialize U for n+1 and U for n-1
U_prev = U_0
U_1 = np.zeros_like(U_0)
data = np.zeros((t_points, n_points, n_points))

######## CENTRAL DIFFERENCE BASED ON SQUARE BOUNDARY CONDITIONS ##############
for t in range(t_points):
    for j in range(1,n_points-1):
        for k in range(1,n_points-1):
            U_1[j][k] = (dt/dx)**2 * (C[j][k])**2 * (U_0[j+1][k] - 4*U_0[j][k] + 
                        U_0[j-1][k] + U_0[j][k+1] + U_0[j][k-1]) + 2*U_0[j][k] - U_prev[j][k]
    data[t] = U_1
    U_prev = U_0.copy() 
    U_0 = U_1.copy() 
########################################################################

####################### PLOT FINAL SURFACE #############################
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
    ax.set_zlim(-2, 2)  # Adjust Z limit if necessary
    ax.set_title(f'Time Frame: {frame + 1}/{num_frames}')
    surf = ax.plot_surface(X, Y, data[frame], cmap='viridis')
    return surf,

# Create animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=50)
###################################################################

plt.show()
