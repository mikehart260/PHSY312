import numpy as np
import scipy.integrate as sci
import matplotlib.pyplot as plt

# N81.14 a-b
# Quantum harmonic oscillator example

hbar2_over_2m = 3.8099e-2 # eV/nm^2

a = 0.01 # nm

def potential(x):
    return 50*x**4/a**4


def rhs_func(x, state, energy):
    psi = state[0]
    phi = state[1]
    rhs_arr = np.zeros_like(state)
    rhs_arr[0] = phi
    rhs_arr[1] = -1/hbar2_over_2m * (energy[0] - potential(x))*psi
    return rhs_arr

def bc_func(state_a, state_b, energy):
    # return np.array([state_a[0], state_b[0], state_a[1] - energy[0]])
    return np.array([state_a[0], state_b[0], state_a[1] - .0000001])


init_x = np.linspace(-10*a,10*a,10) # guess

init_state = np.zeros((2,10))
init_state[0,4:5] = 100.0
init_state[0,3] = 50
init_state[0,6] = 50

init_E = 2000

sol = sci.solve_bvp(rhs_func, bc_func, init_x, init_state, p=(init_E,))

print(sol.p[0])
print(np.sqrt(hbar2_over_2m*2*50/a**2))

plt.close('all')

# plt.plot(sol.x, sol.y[0,:], '-b')
plt.plot(np.linspace(-10*a,10*a, 1000), sol.sol(np.linspace(-10*a,10*a,1000))[0], '-g')
plt.show()
