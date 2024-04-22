import matplotlib.pyplot as plt 
import numpy as np

# plot conic section 
c = 5
e = 0.5
theta_0 = np.pi/3
theta = np.linspace(0, 2*np.pi, 60)

x = np.cos(theta)*c/(1-e*np.cos(theta-theta_0))
y = np.sin(theta)*c/(1-e*np.cos(theta-theta_0))
# plt.polar(theta, c/(1-e*np.cos(theta-theta_0)))
plt.plot(x,y)
plt.show()