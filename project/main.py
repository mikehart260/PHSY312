import numpy as np
import scipy.integrate as sci
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
# project code due 4/24

L = 5
t0 = 0
tf = 5
n_points = 50
t_points = 1000

dx = L/n_points
dt = (tf - t0)/t_points

# wavespeed
C = 3*np.ones((n_points,n_points))

# set up initial conditions.
U_0 = np.ones((n_points,n_points))

for j in range(n_points):
    for k in range(n_points):
        if j == n_points-1 or k == n_points-1 or j == 0 or k == 0:
             U_0[j][k] = 0

# initialize U for n+1 and U for n-1
U_prev = U_0
U_1 = np.zeros_like(U_0)

data = np.zeros((t_points, n_points, n_points))

# find U for n
for t in range(t_points):
    for j in range(1,n_points-1):
        for k in range(1,n_points-1):
            U_1[j][k] = (dt/dx)**2 * (C[j][k])**2 * (U_0[j+1][k] - 4*U_0[j][k] + 
                        U_0[j-1][k] + U_0[j][k+1] + U_0[j][k-1]) + 2*U_0[j][k] - U_prev[j][k]
    data[t] = U_1
    U_prev = U_0.copy() 
    U_0 = U_1.copy() 
    # U_1 = np.zeros_like(U_0)

num_frames = t_points

# plotting initial conditions
X, Y = np.meshgrid(np.linspace(0,L,n_points), np.linspace(0,L,n_points))

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(X, Y, data[-1])

# Function to update the plot for each frame
# def update(frame):
#     ax.clear()
#     ax.set_zlim(-10, 10)  # Adjust Z limit if necessary
#     ax.set_title(f'Time Frame: {frame + 1}/{num_frames}')
#     surf = ax.plot_surface(X, Y, data[frame], cmap='viridis')
#     return surf,

# # Create animation
# ani = FuncAnimation(fig, update, frames=num_frames, blit=True)

# Show the animation
plt.show()
