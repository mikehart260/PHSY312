import numpy as np
import scipy.integrate as sci
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

'''

'''


def initial_condition(i, j):
    x = i*dx
    y = j*dx
    return np.sin(np.pi*y)

def natural_frequencies(n, m):
    return wavespeed_m_s*np.sqrt((n*np.pi/L)**2 + (m*np.pi/L)**2)

### Constant a
def func_to_integrate(y, x, n, m):
    # initial condition * sin(x)*sin(y)
    I = np.sin(np.pi*y)*np.sin(n*np.pi*x/L)*np.sin(m*np.pi*y/L)
    return I

def gfun(x):
    return 0

def hfun(x):
    return L

def constant_a(n, m):
    integral, _ = sci.dblquad(func_to_integrate, 0, L, gfun, hfun,args=(n,m,))
    return 4/L**2 * integral

def func(i, j, t, n, m):
    x = i*dx
    y = j*dx
    a = A[i][j]
    n = 1
    m = 1
    sum = 0
    while (n < 10):
        while (m < 10):
            sum += a * np.cos(natural_frequencies(n,m)*t)*np.sin(n*np.pi*x/L)*np.sin(m*np.pi*y/L)
            m += 1
        n += 1
        m = 0
    return sum

L = 15
t0 = 0
tf = 5
n_points = 50
t_points = 100
n = 2
m = 2

dx = L/n_points # grid spacing 0.1m
dt = (tf - t0)/t_points

wavespeed_m_s = 2 # wavespeed

# constant wavespeed grid
C = wavespeed_m_s*np.ones((n_points,n_points))

U_0 = np.zeros((n_points, n_points))

#### Build constant a matrix once
A = np.zeros_like(U_0)
for i in range(0,n_points):
    for j in range(0,n_points):
        A[i][j] = constant_a(n,m)

##### Initial Condition Grid
for i in range(1,n_points-1):
    for j in range(1,n_points-1):
        U_0[i][j] = initial_condition(i,j)


plt.pcolormesh(U_0)
plt.colorbar()
plt.show()

U_1 = np.zeros_like(U_0)
data = np.zeros((t_points, n_points, n_points))

for t in range(t_points):
    for i in range(1, n_points-1):
        for j in range(1, n_points-1):
            u = func(i, j, t, 1, 1)
            U_1[i][j] = u*5e16
    data[t] = U_1

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
    ax.set_zlim(-0.5, 0.5)  # Adjust Z limit if necessary
    ax.set_title(f'Time Frame: {frame + 1}/{num_frames}')
    surf = ax.plot_surface(X, Y, data[frame], cmap='viridis')
    return surf,

# Create animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=10)
###################################################################

plt.show()
