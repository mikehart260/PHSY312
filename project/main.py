# project code due 4/24
# import scipy.constants as constants
# import scipy.special as special
# import scipy.integrate as integrate
# import matplotlib.pyplot as plt
# import numpy as np



# # test for my poster

# t = np.linspace(0,10,1000)



# plt.plot(t,response(t,intensity,freq,2*collision), label='response')
# plt.plot(t, np.exp(-t*2*collision), ls='dashed', label='decay')
# plt.title("Sample MRF")
# plt.xlabel("Time")
# plt.ylabel("Intensity A.u.")
# plt.legend()
# plt.show()

import numpy as np
import matplotlib.pyplot as plt



# Define the functions to convolve
def f(x):
    return 2*np.exp(-x**2)

def g(x):
    return 2*np.exp(-(x+1)**2)  

intensity = 1
freq = 2*np.pi
collision = 0.5

def response(t):
    return intensity*np.exp(t*(1j*freq - 0.5*collision))

# Define the convolution function
def convolution(f, g, h, x):
    result = np.convolve(f(x), g(x), h(x) ,mode='same') * (x[1] - x[0]) # Scale by delta_x
    return result

# Define the range and step size for x
x = np.linspace(-5, 5, 1000)

# Compute the convolution of f and g
conv_result = convolution(f, response, g ,x)

# Plot the original functions and the convolution
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(x, f(x), label='f(x) = exp(-x^2)')
plt.legend()
plt.title('Original Functions')

plt.subplot(3, 1, 2)
plt.plot(x, response(x), label='response(x)')
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(x, conv_result, label='f * g (Convolution)')
plt.legend()

plt.tight_layout()
plt.show()
 