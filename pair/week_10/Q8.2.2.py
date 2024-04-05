import scipy.integrate as spi
import matplotlib.pyplot as plt
import numpy as np

# 8.2.2
  
# fxn = lambda x: np.sqrt(x)*np.sqrt(1+(0.5*x**(-1/2))**2)

# print(2*np.pi*spi.quad(fxn,0,1)[0])
# print(np.pi*(5**(3/2)-1)/6)

# N5.2

# def fx(x):
#     return x**4 - 2*x + 1

# a , b = 0, 2
# N = 10

# x = np.linspace(a,b,1000)
# simp_val = spi.simpson(fx(x) ,x ,N)
# print(simp_val)
# print(simp_val/4.4 - 1)

# N5.14
