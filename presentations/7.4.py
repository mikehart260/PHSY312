import matplotlib.pyplot as plt

# fig, ax = plt.subplots()

# ax.text(x,y,s) # data coordinate

# transform = ax.transAxes to use axis coordinate

# ax.annotate()
'''
s, string text label
xy, (x, y) coords where the arrow points
xytext, (x, y) coords where the arrow points from (can be left blank)
xycoords, optional string determining type of coords refered to by xy argument. (data, fig fraction, axes fraction)
textcoords, same as xycoords but for xytext argument
arrowprops, determines properties and style of arrow drawn
'''

 # ax.hlines() ; ax.vlines()
'''
Static lines
hlines -> y, xmin, xmax
vlines -> x, ymin, ymax
'''

# ax.axhline() ; ax.axvline()
'''
Dynamic lines - multiple lines require seperate calls
xmin,xmax and ymin, ymax are in fractional axis coordinates so they work well with interactive plots.

Example 7.16 on page 329-330 (EM Spectrum) for more. 
'''

#############
## PATCHES ##
#############
from matplotlib.patches import Circle,Rectangle,Ellipse,Polygon
red, blue, yellow, green, ran = '#ff0000','#0000ff', '#ffff00','#00ff00', '#FF10F0'

circle = Circle((0.8,0.8), 0.15, fc=red) # (xy , radius, **kwargs)
ellipse = Ellipse((0.3,0.8),.2,.25,45,fc=ran)
square = Rectangle((0.75,0.1),0.25,0.25, 30,fc=blue)
 # (lower left coord, width, height, angle, **kwargs) 
# NOTE: angle will soon be a keyword argument.

triangle = Polygon(((0.05,0.1),(0.396,0.1),(0.223,0.38)), fc=yellow)
 # (array of tuples for each vertex, **kwargs)
rhombus = Polygon(((0.5,0.2),(0.7,0.525),(0.5,0.85),(0.3,0.525)), fc=green) 
# (array of tuples for each vertex, **kwargs)

fig = plt.figure(facecolor='k')
ax = fig.add_subplot(aspect='equal')
ax.axis('off')

for shape in (circle, square, triangle, rhombus,ellipse):
    ax.add_patch(shape)

plt.show()

