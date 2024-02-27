import numpy as np

'''
Q6.1.5
[[1, 4]
 [45, 48]]


a = np.linspace(1, 48, 48).reshape(3, 4, 4)

print((a[[0,2],[0,3],:])[:,[0,3]])

''' 
'''
Q6.1.10

Write a one-line statement that returns True if an array is a monotonically increasing sequence or False otherwise.
Hint: np.diff returns the difference between consecutive elements of a sequence. 

For example, 

> np.diff([1, 2, 3, 3, 2])
< array([ 1, 1, 0, -1])
'''
# x = np.array([1,2,0,-1])

# print(np.all((np.diff(x) > 0)))

'''
P 6.1.2

'''
def shoelace(points):
    # 2D points
    N,z = np.shape(points)
    points = np.append(points, points[0]).reshape(N+1,2)
    print(points)
    # multiply diagonals.
    a = [prod for ]
    return 0

N =4
shoe = np.array([[0, 1], [1,2], [4,3], [5,6], [9,0]])
shoelace(shoe)


