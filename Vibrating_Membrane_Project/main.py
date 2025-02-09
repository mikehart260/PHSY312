import numpy as np
import scipy.integrate as sci
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from matplotlib.animation import PillowWriter


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

def initial_condition_sin(i, j):
    x = i*dx
    y = j*dx
    return np.sin(5*np.pi*y)


L = .05
t0 = 0
tf = 1
n_points = 40
t_points = 200


dx = L/n_points # spacial resolution
dt = (tf - t0)/t_points # temporal resolution

wavespeed_m_s = 0.05 # wavespeed

# propagation speed. 
C = wavespeed_m_s*np.ones((n_points,n_points))

#%%%%%%%%%%%%%% CHOOSE ONE INITIAL STATE FROM THE OPTIONS BELOW %%%%%%%%%%%%%%%%%

####### UNIFORM INITIAL STATE WITH SQUARE BOUNDARY CONDITIONS ######
# U_0 = np.ones((n_points, n_points))
# plot_title = "Uniform Initial Condition on Square Boundary"
# for j in range(n_points):
#     for k in range(n_points):
#         if j == n_points-1 or k == n_points-1 or j == 0 or k == 0:
#              U_0[j][k] = 0
##################################################################

####### NORMAL MODE EXCITATION INITIAL CONDITION #################

amplitude = 1
mode_x = 4
mode_y = 4
plot_title = f"Normal mode n={mode_x}, m={mode_y}"
U_0 = np.zeros((n_points, n_points))
for i in range(n_points):
    for k in range(n_points):
      x = i * L/(n_points-1)
      y = k * L/(n_points-1)
      U_0[i][k] = amplitude * np.sin( np.pi * mode_x * x / L ) * np.sin( np.pi * mode_y * y/L)
'''
how to convert grid points to (x,y)
0 - n
|   |
n - n,n

each point should be 1/L 

real x,y origin is n/2, n/2
'''


####### SIN(X) INITIAL STATE WITH SQUARE BOUNDARY CONDITIONS ######
# U_0 = np.ones((n_points, n_points))
# plot_title = "Sin(x) Initial Condition on Square Boundary"
# for j in range(1,n_points-1):
#     for k in range(1,n_points-1):
#         U_0[j][k] = initial_condition_sin(j,k)

# plt.pcolormesh(U_0)
# plt.colorbar()
# plt.show()

####### SET UP DELTA FUNCTION INITIAL STATE WITH SQUARE BOUNDARY CONDITIONS ######
# U_0 = np.zeros((n_points, n_points))
# x_coordinate = np.floor(n_points / 2, casting='same_kind').astype(int) # x coordinate for delta function in terms of L
# y_coordinate = np.floor(n_points / 2, casting='same_kind').astype(int) # y coordinate for delta function in terms of L

# delta_magnitude = 4
# plot_title = "Delta Function on Square Boundary"
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

#%%%%%%%%% Select Boundary Condition Based on The Type of Initial Condition Selected %%%%%%%%%%%%%%%%
######## CENTRAL DIFFERENCE FOR SQUARE BOUNDARY CONDITIONS ##############
for t in range(t_points):
    for j in range(1,n_points-1):
        for k in range(1,n_points-1):
            U_1[j][k] = (dt/dx)**2 * (C[j][k])**2 * (U_0[j+1][k] - 4*U_0[j][k] + 
                        U_0[j-1][k] + U_0[j][k+1] + U_0[j][k-1]) + 2*U_0[j][k] - U_prev[j][k]
    data[t] = U_1
    U_prev = U_0.copy() 
    U_0 = U_1.copy() 
##############################################################################

####### CENTRAL DIFFERENCE FOR TRIANGLE BOUNDARY CONDITIONS ############
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
fig.set_layout_engine('tight')
fig.set_facecolor('white')
ax.set_facecolor('white')


# ax.plot_surface(X, Y, data[0]) # plot initial surface

# ax.plot_surface(X, Y, data[40], facecolors=colors, linewidth=0) # plot final surface
########################################################################

########################## ANIMATION ###################################
num_frames = t_points
data_abs = np.abs(data)

interval = 10 # time between frames in ms

fps = num_frames / interval * 1000
print(fps)

# Function to update the plot for each frame
def update(frame):
    ax.clear()
    ax.set_title(plot_title)
    ax.axis('off')
   # ax.set_title(f'Time Frame: {frame + 1}/{num_frames}')
    ax.set_zlim(-np.max(U_0), np.max(U_0))  # Adjust Z limit if necessary   

    surf = ax.plot_surface(X, Y, data[frame], cmap='RdBu')
    return surf,

# Create animation

ani = FuncAnimation(fig, update, frames=num_frames, interval=interval)

###################################################################

# Save the animation as a gif. 
writer = PillowWriter(fps=30, metadata=dict(artist='Me'), bitrate=1800)
ani.save('Vibrating_Membrane_Project/gifs/normal_mode.gif', writer=writer)


plt.show()
