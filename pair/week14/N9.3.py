from numpy import empty,zeros,max
from pylab import pcolormesh,gray,show,colorbar

# Constants
M = 100         # Grid squares on a side
V = 0.0         # Voltage at top wall
target = 1e-3   # Target accuracy

# Create arrays to hold potential values
phi = zeros([M+1,M+1],float)
phi[0,:] = V
phi[:,0] = V
phi[-1,:] = V
phi[:,-1] = V
phi[20:81,20] = 1
phi[20:81,80] = -1

phiprime = empty([M+1,M+1],float)
omega = 0.9

# Main loop
delta = 1.0
while delta>target:

    # Calculate new values of the potential
    for i in range(M+1):
        for j in range(M+1):
            if i==0 or i==M or j==0 or j==M or (j == 20 and (i >= 20 and i <= 80) or (j == 80 and ((i >= 20 and i <= 80)))):
                phiprime[i,j] = phi[i,j]
            else:
                phiprime[i,j] = (1+omega)*(phi[i+1,j] + phiprime[i-1,j] \
                                 + phi[i,j+1] + phiprime[i,j-1])/4 - omega*phi[i,j]

    # Calculate maximum difference from old values
    delta = max(abs(phi-phiprime))

    # Swap the two arrays around
    phi,phiprime = phiprime,phi

# Make a plot
pcolormesh(phi)
colorbar()
gray()
show()