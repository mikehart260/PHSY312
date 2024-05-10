# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt

r0 = 0.0
rf = 5.0 
n_r = 50

x_1d = np.linspace(r0, rf, n_r)
delta_x = x_1d[1] - x_1d[0]

t0 = 0.0
tf = 12000
n_t = 2000

t_1d = np.linspace(t0, tf, n_t)
delta_t = t_1d[1] - t_1d[0]

Tc = 300.0
Th = 600.0 

Temps = np.zeros([n_r, n_t])

Temps[:,0] = Th
Temps[-1,:] = Tc

kappa = 1.1e-4

for j in range(1,n_t):
    for i in range(1, n_r-1):
        Temps[i,j] = (Temps[i,j-1] + kappa*delta_t/delta_x**2 * (Temps[i+1,j-1]
                                                                -2*Temps[i,j-1]
                                                                +Temps[i-1,j-1]) + kappa/x_1d[i]*delta_t/delta_x*(Temps[i+1,j-1]
                                                                                                                  -Temps[i-1,j-1]))
    Temps[0,j] = Temps[1,j]

plt.close('all')        
plt.pcolormesh(x_1d, t_1d, Temps.transpose()) 
plt.xlabel('Position (m)')
plt.ylabel('Time (s)')
plt.colorbar()
plt.show()
plt.figure()
plt.plot(x_1d, Temps[:,0],label='T=0')
plt.plot(x_1d, Temps[:,-1],label='T=1')
plt.legend()
plt.show()