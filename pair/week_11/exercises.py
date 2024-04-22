
import numpy as np
import scipy.integrate as sci
import matplotlib.pyplot as plt
# 8.1 Low pass Filter

# RC = [.01, ] 
# t0 = 0.0
# tf = 10.0
# nsteps = 100
# t = np.linspace(t0,tf,nsteps)
# V_in = np.zeros(nsteps)
# # for i in t:
# #     if np.floor(2*t)%2 == 0:
# #         V_in[i] = 1
# #     else:
# #         V_in[i] = -1

# def rhs_func(t, state, RC):
#     Vout = state
#     if np.floor(2*t)%2 == 0:
#         return 1/(RC)*(1 - Vout)
#     else:
#         return 1/(RC)*(-1-Vout)

# sol1=sci.solve_ivp(rhs_func,(0,10),[0],args=(0.01,))
# sol2=sci.solve_ivp(rhs_func,(0,10),[0],args=(0.1,))
# sol3 =sci.solve_ivp(rhs_func,(0,10),[0],args=(1,))
# plt.plot(sol1.t,sol1.y[0,:], label="RC = 0.01")
# plt.plot(sol2.t,sol2.y[0,:], label="RC = 0.1")
# plt.plot(sol3.t,sol3.y[0,:], label="RC = 1")
# plt.legend(draggable='true')
# plt.show()


# N8.2
k1 = 3e-12
k2 = 1.2e-33
k3 = 5.5e-4
k4 = 6.9e-16
m = 9e17


def rhs_func(t, state):
    O2 = state[0]
    O = state[1]
    O3 = state[2]
    rhs = np.zeros(3)
    rhs[0] = -k1*O2 - k2*O2*O*m +k3*O3+2*k4*O*O3
    rhs[1] = 2*k1*O2 - k2*O2*O*m + k3*O3 - k4*O*O3
    rhs[2] = k2*O2*O*m - k3*O3 - k4*O*O3
    return rhs

O2_0 = .21*m
O_0 = 0
O3_0 = 0
sol = sci.solve_ivp(rhs_func, (0,10e8), (O2_0,O_0,O3_0), method="Radau")

plt.plot(sol.t, sol.y[0], label = 'O2')
plt.plot(sol.t, sol.y[1], label = "O")
plt.plot(sol.t, sol.y[2], label = "O3")
plt.plot(sol.t, np.sqrt(m*k1*k2/(k3*k4))*sol.y[0], label='O3 approx.')

plt.yscale('log')
plt.xscale('log')

plt.legend(draggable='true')
plt.show()
# P8.2.6
