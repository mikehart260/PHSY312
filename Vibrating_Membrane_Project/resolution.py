import numpy as np
import scipy.integrate as sci
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

L = 1
t0 = 0
tf = 100
n_points = 50
t_points = 500

dx = L/n_points # grid spacing
dt = (tf - t0)/t_points

wavespeed_m_s = 0.07 # wavespeed

# constant wavespeed grid
C = wavespeed_m_s*np.ones((n_points,n_points))

####### SET UP DELTA FUNCTION INITIAL STATE WITH SQUARE BOUNDARY CONDITIONS ######
U_0 = np.zeros((n_points, n_points))
x_coordinate = n_points//2 # x coordinate for delta function in terms of L
y_coordinate = n_points//2 # y coordinate for delta function in terms of L
delta_magnitude = 2

U_0[x_coordinate][y_coordinate] = -delta_magnitude
U_0[x_coordinate+1][y_coordinate+1] = -delta_magnitude/2
U_0[x_coordinate][y_coordinate+1] = -delta_magnitude/2
U_0[x_coordinate+1][y_coordinate] = -delta_magnitude/2
U_0[x_coordinate-1][y_coordinate] = -delta_magnitude/2
U_0[x_coordinate][y_coordinate-1] = -delta_magnitude/2
U_0[x_coordinate-1][y_coordinate-1] = -delta_magnitude/2
U_0[x_coordinate+1][y_coordinate-1] = -delta_magnitude/2
U_0[x_coordinate-1][y_coordinate+1] = -delta_magnitude/2

####### PLOT INITIAL CONDITION
X, Y = np.meshgrid(np.linspace(0,L,n_points), np.linspace(0,L,n_points))

colortuple = ('y', 'b')
colors = np.empty(X.shape, dtype=str)
for y in range(len(Y)):
    for x in range(len(X)):
        colors[y, x] = colortuple[(x + y) % len(colortuple)]

# fig1, ax1 = plt.subplots(subplot_kw={"projection": "3d"})
# surf1 = ax1.plot_surface(X, Y, U_0, cmap='viridis')
# ax1.set_title("Initial Condition")
# plt.show()

######### INITILIZE U FOR n-1 AND n+1
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

####################### PLOT #############################

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
########################## ANIMATION ###################################
num_frames = 500
# Function to update the plot for each frame
def update(frame):
    ax.clear()
    ax.set_zlim(-2, 2)  # Adjust Z limit if necessary
    ax.set_title(f'(dt/dx *c)^2 = {(dt*wavespeed_m_s/dx)**2:.2f} \nTime Frame: {frame + 1}/{num_frames}')
    ax.text(0.5,0.5,0.5,s=f'dt={dt}s, dx={dx}m' ,horizontalalignment='center', verticalalignment='center',transform=ax.transAxes)
    surf = ax.plot_surface(X, Y, data[frame], cmap='viridis')
    return surf,

# Create animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=10)
###################################################################

plt.show()
