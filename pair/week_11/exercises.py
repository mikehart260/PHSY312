# P8.2.6
import numpy as np
import matplotlib.pyplot as plt


RC = [.01, ] 
t0 = 0.0
tf = 10.0
nsteps = 100
t = np.linspace(t0,tf,nsteps)
V_in = np.zeros(nsteps)
for i in t:
    if np.floor(2*t)%2 == 0:
        V_in[i] = 1
    else:
        V_in[i] = -1

def rhs_func(Vout, t):
    return 1/(RC)(V_in - Vout)