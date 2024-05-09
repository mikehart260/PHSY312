import numpy as np
import scipy.integrate as sci
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib as mpl


methods = ['RK45','LSODA']
method = methods[0]
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
t_stop = 102*yr
dt = day
t = np.arange(0, t_stop, dt)

def rhs_func(time, state, M1, M2, M3):
    x1 = state[0] # dx1/dt 
    A = state[1] #  dA/dt
    y1 = state[2] 
    B = state[3]
    z1 = state[4]
    C = state[5]
    x2 = state[6]
    D = state[7]
    y2 = state[8]
    E = state[9]
    z2 = state[10]
    F = state[11]
    x3 = state[12]
    G_ = state[13]
    y3 = state[14]
    H = state[15]
    z3 =state[16]
    I = state[17]

    rhs_arr = np.zeros(len(state))
    
    # body 1
    rhs_arr[0] = A
    rhs_arr[1] = G*M2*(x2 - x1) / (np.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2))**3 + G*M3*(x3-x1)/(np.sqrt((x3-x1)**2 + (y3-y1)**2 + (z3-z1)**2))**3
    rhs_arr[2] = B
    rhs_arr[3] = G*M2*(y2 - y1) / (np.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2))**3 + G*M3*(y3-y1)/(np.sqrt((x3-x1)**2 + (y3-y1)**2 + (z3-z1)**2))**3
    rhs_arr[4] = C 
    rhs_arr[5] = G*M1*(z2 - z1) / (np.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2))**3 + G*M3*(z3-z1)/(np.sqrt((x3-x1)**2 + (y3-y1)**2 + (z3-z1)**2))**3
   
    # body 2
    rhs_arr[6] = D
    rhs_arr[7] = G*M1*(x1 - x2) / (np.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2))**3 + G*M3*(x3-x2)/(np.sqrt((x3-x2)**2 + (y3-y2)**2 + (z3-z2)**2))**3
    rhs_arr[8] = E
    rhs_arr[9] = G*M1*(y1 - y2) / (np.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2))**3 + G*M3*(y3-y2)/(np.sqrt((x3-x2)**2 + (y3-y2)**2 + (z3-z2)**2))**3
    rhs_arr[10] = F
    rhs_arr[11] = G*M1*(z1 - z2) / (np.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2))**3 + G*M3*(z3-z2)/(np.sqrt((x3-x2)**2 + (y3-y2)**2 + (z3-z2)**2))**3
    
    # body 3
    rhs_arr[12] = G_
    rhs_arr[13] = G*M1*(x1 - x3) / (np.sqrt((x1-x3)**2 + (y1-y3)**2 + (z1-z3)**2))**3 + G*M2*(x2-x3)/(np.sqrt((x3-x2)**2 + (y3-y2)**2 + (z3-z2)**2))**3
    rhs_arr[14] = H
    rhs_arr[15] = G*M1*(y1 - y3) / (np.sqrt((x1-x3)**2 + (y1-y3)**2 + (z1-z3)**2))**3 + G*M2*(y2-y3)/(np.sqrt((x3-x2)**2 + (y3-y2)**2 + (z3-z2)**2))**3
    rhs_arr[16] = I
    rhs_arr[17] = G*M1*(z1 - z3) / (np.sqrt((x1-x3)**2 + (y1-y3)**2 + (z1-z3)**2))**3 + G*M2*(z2-z3)/(np.sqrt((x3-x2)**2 + (y3-y2)**2 + (z3-z2)**2))**3
    return rhs_arr

m1 = sun
m2 = sun
m3 = sun

# inital conditions

# GOOD Conditions
# xx2 = 1.5*au # x position of mass 2
# xy2 = au # y position of mass 2
# xz2 = au # z position of mass 2
# vx2 = 5000 # velocity in x dir of mass 2
# vy2 =  0 # velocity in y dir of mass 2
# vz2 = 0 # vel in z dir of mass 3

# xx1 = -au # x position of mass 1
# xy1 = -1.5*au # y position of mass 1
# xz1 = 0 # z position of mass 1
# vx1 = -10000 # velocity in x dir of mass 1
# vy1 = 0 # velocity in y dir of mass 1
# vz1 = 0 # vel in z dir of mass 1

######################################

xx2 = 1.5*au # x position of mass 2
xy2 = au # y position of mass 2
xz2 = au # z position of mass 2
vx2 = 0 # velocity in x dir of mass 2
vy2 =  0 # velocity in y dir of mass 2
vz2 = 0 # vel in z dir of mass 3

xx1 = -au # x position of mass 1
xy1 = -1.5*au # y position of mass 1
xz1 = 0 # z position of mass 1
vx1 = 0 # velocity in x dir of mass 1
vy1 = 0 # velocity in y dir of mass 1
vz1 = 0 # vel in z dir of mass 1



xx3 = - (m1*xx1 + m2*xx2) / m3 # x pos of mass 3
xy3 = - (m1*xy1 + m2*xy2) / m3 # y pos of mass 3
xz3 = - (m1*xz1 + m2*xz2) / m3 # z pos of mass 3
vx3 = - (m1*vx1 + m2*vx2) / m3 # vel in x dir of mass 3
vy3 = - (m1*vy1 + m2*vy2) / m3 # vel in y dir of mass 3
vz3 = - (m1*vz1 + m2*vy2) / m3 # vel in z dir of mass 3


sol = sci.solve_ivp(rhs_func, t[[0, -1]], [xx1, vx1, xy1, vy1, xz1, vz1, xx2, vx2, xy2, vy2, xz2, vz2, xx3, vx3, xy3, vy3, xz3, vz3], t_eval=t , args=(m1, m2, m3,), method=method)

xpos_1 = sol.y[0]
xvel_1 = sol.y[1]
ypos_1 = sol.y[2]
yvel_1 = sol.y[3]
zpos_1 = sol.y[4]
zvel_1 = sol.y[5]
xpos_2 = sol.y[6]
xvel_2 = sol.y[7]
ypos_2 = sol.y[8]
yvel_2 = sol.y[9]
zpos_2 = sol.y[10]
zvel_2 = sol.y[11]
xpos_3 = sol.y[12]
xvel_3 = sol.y[13]
ypos_3 = sol.y[14]
yvel_3 = sol.y[15]
zpos_3 = sol.y[16]
zvel_3 = sol.y[17]

# sep_distance = [np.sqrt( (x_1 - x_2 )**2 + (y_1 - y_2 )**2) for x_1,x_2,y_1,y_2 in zip(x1,x2,y1,y2)]

#angle = [np.arccos( (x_1*x_2 + y_1*y_2) / ( np.sqrt(x_1**2 + y_1**2) * np.sqrt(x_2**2 + y_2**2) ) )
#         for x_1,x_2,y_1,y_2 in zip(x1,x2,y1,y2)]
#r_x = [np.cos(theta)*r for theta,r in zip(angle,sep_distance) ]
#r_y = [np.sin(theta)*r for theta,r in zip(angle,sep_distance)]

mpl.rcParams['grid.color'] = 'k'
mpl.rcParams['grid.linestyle'] = ':'
mpl.rcParams['grid.linewidth'] = 0.5
fig = plt.figure(figsize=(6, 5))
ax = fig.add_subplot(autoscale_on=False, xlim=(-3.5*au, 3.5*au), ylim=(-3.5*au, 3.5*au), zlim = (-3.5*au, 3.5*au) ,projection='3d')
ax.set_aspect('equal')
ax.grid('off')

line1, = ax.plot([],[],[], 'o', ms = np.ceil(15*m1/sun), c='#13EAC9')
line2, = ax.plot([],[],[], 'o', ms = np.ceil(15*m2/sun), c='#C20078')
line3, = ax.plot([],[],[], 'o', ms = np.ceil(15*m3/sun), c='#BBE90F')
# conic_trace, = ax.plot([],[], '.-', label='conic')
r_trace, = ax.plot([], [], '.-')
trace1, = ax.plot([], [], '.-', lw=1, ms=2, c='b')
trace2, = ax.plot([],[], '.-', lw=1, ms=2, c='m')
trace3, = ax.plot([],[], '.-', lw=1, ms=2, c='g')
time_template = 'time = %0.1f years'
time_text = ax.text(0.05, 0.9, 1,'', transform=ax.transAxes)

def animate(i):
    thisx = [xpos_1[i], xpos_2[i], xpos_3[i]]
    thisy = [ypos_1[i], ypos_2[i], ypos_3[i]]
    thisz = [zpos_1[i], zpos_2[i], zpos_3[i]]
    #history_rx = r_x[:i]
    #history_ry = r_y[:i]
    idx = 0
    if i > 150:
        idx = i-150
    else:
        idx = 0

    history_x1 = xpos_1[idx:i]
    history_y1 = ypos_1[idx:i]
    history_z1 = zpos_1[idx:i]
    history_x2 = xpos_2[idx:i]
    history_y2 = ypos_2[idx:i]
    history_z2 = zpos_2[idx:i]
    history_x3 = xpos_3[idx:i]
    history_y3 = ypos_3[idx:i]
    history_z3 = zpos_3[idx:i]
    
    line1.set_data([thisx[0]] ,[thisy[0]]) # mass 1
    line2.set_data([thisx[1]], [thisy[1]] ) # mass 2
    line3.set_data([thisx[2]], [thisy[2]]) # mass 3
    line1.set_3d_properties([thisz[0]])
    line2.set_3d_properties([thisz[1]])
    line3.set_3d_properties([thisz[2]])

    # conic_trace.set_data(history_rx, history_ry) # conic circles line.
    trace1.set_data(history_x1, history_y1) # tracing mass 1 motion
    trace2.set_data(history_x2, history_y2) # tracing mass 2 motion
    trace3.set_data(history_x3, history_y3) # tracing mass 3 motion
    trace1.set_3d_properties(history_z1)
    trace2.set_3d_properties(history_z2)
    trace3.set_3d_properties(history_z3)

    time_text.set_text(time_template % (i*dt/day/356)) 
    return line1, line2, line3, trace1, trace2, trace3, time_text

print(len(xpos_1))

ani = animation.FuncAnimation(
    fig, animate, len(xpos_1), interval = 10 ,blit=True)

plt.show()

# Total Energy
v1 = np.sqrt(xvel_1**2 + yvel_1**2 + zvel_1**2)
v2 = np.sqrt(xvel_2**2 + yvel_2**2 + zvel_2**2)
v3 = np.sqrt(xvel_3**2 + yvel_3**2 + zvel_3**2)

sep_1_2 = np.sqrt((xpos_2-xpos_1)**2 + (ypos_2-ypos_1)**2 + (zpos_2-zpos_1)**2)
sep_1_3 = np.sqrt((xpos_1-xpos_3)**2 + (ypos_1-ypos_3)**2 + (zpos_1-zpos_3)**2)
sep_2_3 = np.sqrt((xpos_3-xpos_2)**2 + (ypos_3-ypos_2)**2 + (zpos_3-zpos_2)**2)

E_tot = 0.5*(m1*v1**2 + m2*v2**2 + m3*v3**2) - G*(m1*m2/sep_1_2 + m1*m3/sep_1_3 + m2*m3/sep_2_3)
print(sol.t[-1]/yr)
plt.plot(sol.t,E_tot)
plt.ylim(-5e40,0)
plt.xlabel("time (yr)")
plt.xticks(yr*np.arange(0,t_stop/yr,10),np.arange(0,t_stop/yr,10))
plt.ylabel("Energy")
plt.title("Total energy vs time")
plt.show()

# Total Momentum
P_tot = m1*v1 + m2*v2 + m3*v3
plt.plot(sol.t, P_tot)
plt.xlabel("time (yr)")
plt.xticks(yr*np.arange(0,t_stop/yr,10),np.arange(0,t_stop/yr,10))
plt.title("momentum")
plt.show()