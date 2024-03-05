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

def neg_circle(x,x_center,y_center,r):
    y = -1*np.sqrt(r**2 - (x-x_center)**2) + y_center
    return y

def pos_circle(x,x_center,y_center,r):
    y = np.sqrt(r**2 - (x-x_center)**2) + y_center
    return y
x_values_1 = np.linspace(x_center-R,x_center+R,int(num_of_imgs/2)) # 10 points on x axis
x_values_2 = x_values_1[::-1]

for num in range(num_of_imgs):
    print(num)
    if num < 10: # first 10 images
        x = x_values_1[num]
        num = '0' + str(num)
        cy = pos_circle(x,x_center,y_center,R)
        print("pos cy: ", cy)
    else:
        if num == 19:
            break
        x = x_values_2[num-9]
        cy = neg_circle(x,x_center,y_center,R)
        print("neg cy: ", cy)

    with open(os.path.join(path,f"file{num}.svg"),'w') as f:
        f.write('<?xml version="1.0" encoding="utf-8"?>\n')
        f.write('<svg xmlns="http://www.w3.org/2000/svg"\n')
        f.write('xmlns:xlink="http://www.w3.org/1999/xlink"\n')
        f.write(f'width="500" height="500" style="background: #ffffff"> <circle cx="{x_center}" cy="{y_center}" r="{R}" style="stroke: black; stroke-width: 2px;\n')
        f.write(f'fill: none;"/> <circle cx="{x}" cy="{cy}" r="20" style="stroke: red; fill: red;"/>\n')
        f.write('</svg>')