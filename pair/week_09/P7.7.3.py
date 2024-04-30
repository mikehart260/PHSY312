import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as pat
import matplotlib.animation as animation

voy_data = np.genfromtxt('/Users/michaelhart/repos/PHSY312/pair/week_09/HORIZONS-trajectories/voyager2.txt',skip_header=48,dtype=str,delimiter='\n',skip_footer=42)


clean_data = []
X_data = []
Y_data = []

vals = []
for line in voy_data:
    vals = []
    if line[0] == 'X':
        line = line.split()
        for elem in line:
            if len(elem) > 1:
                if elem[0] == '=':
                    elem = elem.replace('=','')
                    vals.append(elem)
                else:
                    vals.append(elem)
        clean_data.append(vals)

for data in clean_data:
    X_data.append(float(data[0]))
    Y_data.append(float(data[1]))




fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ball = pat.Circle((0, 0), 0.08)
xdata, ydata = [], []

ax.add_patch(ball)
interval = 1

# def init():
#     line.set_data(xdata, ydata)
#     return line,

def animate(pos):
    ball.set_center(())
    line.set_data(xdata, ydata)
    return line, ball 

def get_pos(t=0):
    for i in range(len(X_data)):
        yield X_data[i], Y_data[i]

am = animation.FuncAnimation(fig, animate, get_pos, blit=True, interval=interval, repeat = False)
plt.show()




