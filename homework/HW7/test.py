import matplotlib.pyplot as plt 
import numpy as np

x1 = np.arange(stop=10,step=1)


sep_distance = [np.sqrt( (x_1 - x_2 )**2 + (y_1 - y_2 )**2) for x_1,x_2,y_1,y_2 in zip(x1,x2,y1,y2)]