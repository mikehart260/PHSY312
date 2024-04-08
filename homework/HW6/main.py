import numpy as np
import scipy.integrate as sci
import matplotlib.pyplot as plt

t, a_x, a_y, a_z = np.genfromtxt('/Users/michaelhart/repos/PHSY312/homework/HW6/v05686txyz-1.txt', unpack=True, dtype=float)

# t = 0 @ index = 2499
t_0_idx = 2499
t = t[t_0_idx:]

a_x_err = np.std(a_x[:t_0_idx+1])
a_y_err = np.std(a_y[:t_0_idx+1])
a_z_err = np.std(a_z[:t_0_idx+1])

delta_t = 0.00008 # [seconds] 

# velocity error propagated
v_x_err = a_x_err * delta_t * np.arange(1,len(t)+1)
v_y_err = a_y_err * delta_t * np.arange(1,len(t)+1)
v_z_err = a_z_err * delta_t * np.arange(1,len(t)+1)

# v_x = integral of a_x and the integration error

v_x = []
v_y = []
v_z = []

v_x_Ierr = []
v_y_Ierr = []
v_z_Ierr = []



for i in range(0,len(t)):
    vx1 = sci.trapezoid(a_x[t_0_idx:t_0_idx+i],t[0:i])
    vx2 = sci.trapezoid(a_x[t_0_idx:t_0_idx+i:2],t[0:i:2])
    vy1 = sci.trapezoid(a_y[t_0_idx:t_0_idx+i],t[0:i])
    vy2 = sci.trapezoid(a_y[t_0_idx:t_0_idx+i:2],t[0:i:2])
    vz1 = sci.trapezoid(a_z[t_0_idx:t_0_idx+i],t[0:i])
    vz2 = sci.trapezoid(a_z[t_0_idx:t_0_idx+i:2],t[0:i:2])
    
    v_x.append(vx1)
    v_y.append(vy1)
    v_z.append(vz1)
    v_x_Ierr.append(np.abs(vx1-vx2)/3)
    v_y_Ierr.append(np.abs(vy1-vy2)/3)
    v_z_Ierr.append(np.abs(vz1-vz2)/3)


# position error propagated
pos_x_err = []
pos_y_err = []
pos_z_err = []

print(len(t))

sumation = np.cumsum(range(0,len(t)+1))


for k in range(len(t)):
    pos_x_err.append(a_x_err * delta_t**2 * sumation[k+1])
    pos_y_err.append(a_y_err * delta_t**2 * sumation[k+1])
    pos_z_err.append(a_z_err * delta_t**2 * sumation[k+1])

# pos_x = integral of v_x and the integration error

pos_x = []
pos_y = []
pos_z = []

pos_x_Ierr = []
pos_y_Ierr = []
pos_z_Ierr = []

for i in range(0,len(t)):
    x1 = sci.trapezoid(v_x[0:i],t[0:i])
    x2 = sci.trapezoid(v_x[0:i:2],t[0:i:2])
    y1 = sci.trapezoid(v_y[0:i],t[0:i])
    y2 = sci.trapezoid(v_y[0:i:2], t[0:i:2])
    z1 = sci.trapezoid(v_z[0:i],t[0:i])
    z2 = sci.trapezoid(v_z[0:i:2], t[0:i:2])

    pos_x.append(x1)
    pos_y.append(y1)
    pos_z.append(z1)

    pos_x_Ierr.append(np.abs(x1-x2)/3)
    pos_y_Ierr.append(np.abs(y1-y2)/3)
    pos_z_Ierr.append(np.abs(z1-z2)/3)

tot_pos_x_err = np.add(np.abs(pos_x_err),np.abs(pos_x_Ierr))
tot_pos_y_err = np.add(np.abs(pos_y_err), np.abs(pos_y_Ierr))
tot_pos_z_err = np.add(np.abs(pos_z_err), np.abs(pos_z_Ierr))
# Plotting
                       
fig, (ax0,ax1,ax2) = plt.subplots(nrows=3,sharex=True)
ax0.errorbar(t , pos_x, yerr = tot_pos_x_err, errorevery=50)
ax0.set_title("X Position")
ax1.errorbar(t , pos_y, yerr = tot_pos_x_err, errorevery=50)
ax1.set_title("Y Position ")
ax2.errorbar(t , pos_z, yerr = tot_pos_z_err, errorevery=50)
ax2.set_title("Z Position ")
plt.xlabel("time")
plt.show()

print(len(v_x))
print(len(v_x_err))
print(len(v_x_Ierr))

tot_v_x_err = np.add(np.abs(v_x_err),np.abs(v_x_Ierr))
tot_v_y_err = np.add(np.abs(v_y_err), np.abs(v_y_Ierr))
tot_v_z_err = np.add(np.abs(v_z_err), np.abs(v_z_Ierr))
fig, (ax0,ax1,ax2) = plt.subplots(nrows=3,sharex=True)
ax0.errorbar(t , v_x, yerr = tot_v_x_err, errorevery=50)
ax0.set_title("X velocity")
ax1.errorbar(t , v_y, yerr = tot_v_x_err, errorevery=50)
ax1.set_title("Y velocity ")
ax2.errorbar(t , v_z, yerr = tot_v_z_err, errorevery=50)
ax2.set_title("Z velocity ")
plt.xlabel("time")
plt.show()

fig, (ax0,ax1,ax2) = plt.subplots(nrows=3,sharex=True)
ax0.errorbar(t , a_x[t_0_idx:], yerr = a_x_err, errorevery=50)
ax0.set_title("X acceleration")
ax1.errorbar(t , a_y[t_0_idx:], yerr = a_y_err, errorevery=50)
ax1.set_title("Y acceleration ")
ax2.errorbar(t , a_z[t_0_idx:], yerr = a_z_err, errorevery=50)
ax2.set_title("Z acceleration ")
plt.xlabel("time")
plt.show()

# Final Position
print( f'X_f = [{pos_x[-1]}, {pos_y[-1]}, {pos_z[-1]}] +/- {pos_x_err[-1]}, +/- {pos_x_Ierr[-1]}')

