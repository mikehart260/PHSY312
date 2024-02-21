import os
import numpy as np
path = os.getcwd()
if (os.path.isdir(os.path.join(path,'svg_files'))):
    print("dir exists")
    path = os.path.join(path,'svg_files')
else:
    print("dir doesn't exist")
    try: 
        os.mkdir(os.path.join(path,'svg_files'))
        path = os.path.join(path,'svg_files')
    except:
        print("error in making dir")
    else: 
        print("dir created ")

#radius
R = 200
num_of_imgs = 20
# circle origin is (250,250)
x_center = 250
y_center = 250

def circle(x,x_center,y_center,r):
    y = np.sqrt(r**2 - (x-x_center)**2) + y_center
    return y
x_values = np.linspace(x_center-R,x_center+R,num_of_imgs+1)

for num in range(num_of_imgs+1):
    x = x_values[num]
    if num < 10:
        num = '0' + str(num)
    with open(os.path.join(path,f"file{num}.svg"),'w') as f:
        f.write('<?xml version="1.0" encoding="utf-8"?>\n')
        f.write('<svg xmlns="http://www.w3.org/2000/svg"\n')
        f.write('xmlns:xlink="http://www.w3.org/1999/xlink"\n')
        f.write(f'width="500" height="500" style="background: #ffffff"> <circle cx="{x_center}" cy="{y_center}" r="{R}" style="stroke: black; stroke-width: 2px;\n')
        f.write(f'fill: none;"/> <circle cx="{x}" cy="{circle(x,x_center,y_center,R)}" r="20" style="stroke: red; fill: red;"/>\n')
        f.write('</svg>')