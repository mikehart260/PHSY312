import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize

G = 6.6674E-11
M = 5.974E24
m = 7.348e22
R = 3.844e8
omega = 2.662e-6



def func(r):

    return G*M/r**2 -G*m/(R-r)**2 -omega**2*r

def d_func_d_x(r):

    return -2*G*M/r**3 -2*G*m/(R-r)**3 - omega**2

x_0 = 1000
x_p = 8e8
tolerance = 1e-1

x_plt = np.linspace(0, 20e8, 1000)

plt.close('all')
plt.plot(x_plt, func(x_plt), 'r-')
plt.ylim((-2,2))
plt.hlines(y=0,xmin= -10,xmax=10)
while np.abs(x_p-x_0) > tolerance:
    plt.scatter(x_p, func(x_p), c='g',marker='*')
    x_p, x_0 = x_p-func(x_p)/d_func_d_x(x_p) , x_p


# root = optimize.brentq(f=func,a=-1,b=2)
# print(root)
plt.show()