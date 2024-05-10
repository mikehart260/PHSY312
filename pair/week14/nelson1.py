import numpy as np
from numpy import empty,zeros,max
from pylab import pcolormesh,gray,show,colorbar

# Constants
M = 100         # Grid squares on a side and length of grid in cm
V = 0.0         # Voltage at boundaries
qp = 10e-9
qn = -10e-9
L_p = 40       # m
L_n = 60
k = 9e9

length = 1      # m
grid_spacing = M / length

# Create charge density grid
x = range(M+1)
y = range(M+1)
X, Y = np.meshgrid(x,y)
sigma_x = 0.5
sigma_y = 0.5
charge_density = qp*np.exp(-((X - L_p)**2 / 2*sigma_x**2 + (Y - 50)**2 / 2*sigma_y**2))
charge_density = charge_density+qn*np.exp(-((X - L_n)**2 / 2*sigma_x**2 + (Y - 50)**2 / 2*sigma_y**2))

analytical = k*qp/(np.sqrt((X-L_p+.1)**2 + Y**2)) + k*qn/(np.sqrt((X+L_n+.1)**2 + Y**2))

#charge_density =  qn*np.exp(-(( X + L)**2 / 2 + (Y + L)**2 / 2)
#pcolormesh(charge_density)
#colorbar()
#show()

target = 1e-4   # Target accuracy

# Create arrays to hold potential values
phi = zeros([M+1,M+1],float)
phi[0,:] = V
phi[:,0] = V
phi[-1,:] = V
phi[:,-1] = V

phiprime = empty([M+1,M+1],float)
omega = 0.8
analytical = np.zeros_like(phiprime)
# Main loop
delta = 1.0
while delta>target:

    # Calculate new values of the potential
    for i in range(M+1):
        for j in range(M+1):
            if i==0 or i==M or j==0 or j==M:
                phiprime[i,j] = phi[i,j]
            else:
                phiprime[i,j] = (1+omega)*(phi[i+1,j] + phiprime[i-1,j] \
                                 + phi[i,j+1] + phiprime[i,j-1])/4 - omega*phi[i,j] + .01**2*9e9*charge_density[i,j]/(np.pi*4)

    # Calculate maximum difference from old values
    delta = max(abs(phi-phiprime))

    # Swap the two arrays around
    phi,phiprime = phiprime,phi

# Make a plot
pcolormesh(phi)
colorbar()

show()
# analytical soln
pcolormesh(analytical)
colorbar()

show()
