import numpy as np
import scipy.integrate as sci
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# constants 
G = 6.67e-11 # N m^2/kg^2
au = 1.5e11 # meters
yr = 3.154e7 # seconds
day = 86400 # seconds
sun = 2e30 # kg
earth = 6e24 # kg
moon = 7.3e22 # kg 
e_speed = 30 # km/s

# time range
t_stop = 2*yr
dt = day
t = np.arange(0, t_stop, dt)

def rhs_func(time, state, M1, M2):
    x1 = state[0] # dx1/dt 
    A = state[1] #  dA/dt
    y1 = state[2] 
    B = state[3]
    x2 = state[4]
    C = state[5]
    y2 = state[6]
    D = state[7]
    
    rhs_arr = np.zeros(8)
    
    rhs_arr[0] = A
    rhs_arr[1] = G*M2*(x2 - x1) / (np.sqrt((x2-x1)**2 + (y2-y1)**2))**3
    rhs_arr[2] = B
    rhs_arr[3] = G*M2*(y2 - y1) / (np.sqrt((x2-x1)**2 + (y2-y1)**2))**3
    rhs_arr[4] = C 
    rhs_arr[5] = G*M1*(x1 - x2) / (np.sqrt((x1-x2)**2 + (y1-y2)**2))**3
    rhs_arr[6] = D
    rhs_arr[7] = G*M1*(y1 - y2) / (np.sqrt((x1-x2)**2 + (y1-y2)**2))**3

    return rhs_arr

m1 = sun
m2 = sun

# inital conditions
xx2 = au # x position of mass 2
xy2 = 0 # y position of mass 2
vx2 = -5000 # velocity in x dir of mass 2
vy2 = -10000 # velocity in y dir of mass 2
xx1 = -au # x position of mass 1
xy1 = 0 # y position of mass 1
vx1 = -1*m2/m1 * vx2 # velocity in x dir of mass 1
vy1 = -1*m2/m1 * vy2 # velocity in y dir of mass 1


sol = sci.solve_ivp(rhs_func, t[[0, -1]], [xx1, vx1, xy1, vy1 ,xx2, vx2, xy2, vy2], t_eval=t ,args=(m1, m2,))

x1 = sol.y[0]
vx1 = sol.y[1]
y1 = sol.y[2]
vy1 = sol.y[3]
x2 = sol.y[4]
vx2 = sol.y[5]
y2 = sol.y[6]
vy2 = sol.y[7]

sep_distance = [np.sqrt( (x_1 - x_2 )**2 + (y_1 - y_2 )**2) for x_1,x_2,y_1,y_2 in zip(x1,x2,y1,y2)]
#angle = [np.arccos( (x_1*x_2 + y_1*y_2) / ( np.sqrt(x_1**2 + y_1**2) * np.sqrt(x_2**2 + y_2**2) ) )
#         for x_1,x_2,y_1,y_2 in zip(x1,x2,y1,y2)]
#r_x = [np.cos(theta)*r for theta,r in zip(angle,sep_distance) ]
#r_y = [np.sin(theta)*r for theta,r in zip(angle,sep_distance)]

fig = plt.figure(figsize=(6, 5))
ax = fig.add_subplot(autoscale_on=False, xlim=(-6*au, 6*au), ylim=(-6*au, 6*au))
ax.set_aspect('equal')

line1, = ax.plot([], 'o', ms = np.ceil(15*m1/sun), c='y')
line2, = ax.plot([], 'o', ms = np.ceil(15*m2/sun), c='b')
# conic_trace, = ax.plot([],[], '.-', label='conic')
r_trace, = ax.plot([], [], '.-')
trace, = ax.plot([], [], '.-', lw=1, ms=2, c='orange')
trace2, = ax.plot([],[], '.-', lw=1, ms=2,c='r')
time_template = 'time = %0.1f years'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

def animate(i):
    thisx = [x1[i], x2[i]]
    thisy = [y1[i], y2[i]]
    #history_rx = r_x[:i]
    #history_ry = r_y[:i]
    history_x1 = x1[:i]
    history_y1 = y1[:i]
    history_x = x2[:i]
    history_y = y2[:i]
    
    line1.set_data([thisx[0]], [thisy[0]]) # mass 1
    line2.set_data([thisx[1]], [thisy[1]]) # mass 2
    # conic_trace.set_data(history_rx, history_ry) # conic circles line.
    trace.set_data(history_x, history_y) # tracing mass 1 motion
    trace2.set_data(history_x1, history_y1) # tracing mass 2 motion
    time_text.set_text(time_template % (i*dt/day/356)) 
    return line1,line2, trace, trace2, time_text

ani = animation.FuncAnimation(
    fig, animate, len(x1), interval = 100 ,blit=True)

# conic shapes
c = au/2
e = 0.5
theta_0 = np.pi
theta = np.linspace(0, 2*np.pi, 60)
x = np.cos(theta)*c/(1-e*np.cos(theta-theta_0))
y = np.sin(theta)*c/(1-e*np.cos(theta-theta_0))
plt.plot(x,y,label='conic shape',c='g')
plt.legend()
plt.show()

# kinetic and potential energy plots
fig2 = plt.figure()
ax2 = fig2.add_subplot()
tot_ke = 0.5*m1*(vx1**2+vy1**2)+0.5*m2*np.sqrt(vx2**2+vy2**2)
tot_pot = -2*G*m1*m2/np.array(sep_distance)
ax2.plot(t,tot_ke,label='kinetic energy')
ax2.plot(t,tot_pot,label='potential energy')
plt.legend()
plt.show()

# total energy plots
plt.plot(t,tot_ke+tot_pot)
plt.show()