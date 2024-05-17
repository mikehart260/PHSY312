import numpy as np
import scipy.integrate as sci
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

def intriangle(j,k,n):
    if (k > n//2 - j and k < n//2 + j):
        return True
    else:
        return False

def triangle_bc(j,k,n):
    if (k <= n//2 - j or k >= n//2 +j):
        return True
    else:
        return False

L = 1
t0 = 0
tf = 60
n_points = 20
t_points = 400


dx = L/n_points # grid spacing
dt = (tf - t0)/t_points

wavespeed_m_s = 0.1 # wavespeed

# constant wavespeed grid
C = wavespeed_m_s*np.ones((n_points,n_points))

####### SET UP UNIFORM INITIAL STATE WITH SQUARE BOUNDARY CONDITIONS ######
U_0 = np.ones((n_points, n_points))

for j in range(n_points):
    for k in range(n_points):
        if j == n_points-1 or k == n_points-1 or j == 0 or k == 0:
             U_0[j][k] = 0
##################################################################

####### SET UP DELTA FUNCTION INITIAL STATE WITH SQUARE BOUNDARY CONDITIONS ######
# U_0 = np.zeros((n_points, n_points))
# x_coordinate = 9 # x coordinate for delta function in terms of L
# y_coordinate = 9 # y coordinate for delta function in terms of L
# delta_magnitude = 1.5

# U_0[x_coordinate][y_coordinate] = -delta_magnitude
##################################################################

######## SET UP UNIFORM INITIAL CONDITION WITH TRIANGLE BOUNDARY CONDITIONS ##############
# U_0 = np.ones((n_points, n_points))
# for j in range(0, n_points):
#     for k in range(0, n_points):
#         if (triangle_bc(j,k,n_points)):
#             U_0[j][k] = 0
##################################################################################

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
##############################################################################

######## CENTRAL DIFFERENCE BASED ON TRIANGLE BOUNDARY CONDITIONS ############
# for t in range(t_points):
#     for j in range(0,n_points-1):
#         for k in range(0,n_points-1):
#             if (intriangle(j,k,n_points)):        
#                 U_1[j][k] = (dt/dx)**2 * (C[j][k])**2 * (U_0[j+1][k] - 4*U_0[j][k] + 
#                         U_0[j-1][k] + U_0[j][k+1] + U_0[j][k-1]) + 2*U_0[j][k] - U_prev[j][k]
#     data[t] = U_1
#     U_prev = U_0.copy() 
#     U_0 = U_1.copy() 
##############################################################################


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
    ax.set_zlim(-2, 2)  # Adjust Z limit if necessary
    ax.set_title(f'Time Frame: {frame + 1}/{num_frames}')
    surf = ax.plot_surface(X, Y, data[frame], cmap='viridis')
    return surf,

# Create animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=10)
###################################################################

plt.show()
