from numpy import polynomial as pol
import numpy as np
import matplotlib.pyplot as plt

x = [1.3, 6.0, 20.2, 43.9, 77.0, 119.6, 171.7, 233.2, 304.2, 384.7, 474.7, 574.1, 683.0, 801.3, 929.2, 1066.4, 1213.2, 1369.4, 1535.1, 1710.3, 1894.9]
t = []
for i in range(len(x)):
    t.append(i*0.1)

t = np.array(t)
x = np.array(x)
x = x*0.01
fit = pol.polynomial.polyfit(np.array(t),x,2)
g = fit[2]*2
print(f'g={g}')
equ = pol.Polynomial(fit)



print(equ)
plt.scatter(t,x,label='data')
plt.plot(t,equ(t), label='fit',color='r')
plt.legend()
plt.show()
