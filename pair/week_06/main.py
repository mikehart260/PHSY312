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


def shoelace(points):
    # 2D points
    N,z = np.shape(points)
    points = np.append(points, points[0]).reshape(N+1,2)
    print(points)
    # multiply diagonals.
    S1 = np.sum([points[i,0]*points[i+1,1] for i in range(0,N)])
    S2 = np.sum([points[i+1,0]*points[i,1] for i in range(0,N)])
    return 0.5*np.abs(S1-S2)

N = 4
shoe = np.array([[0, 1], [1,2], [4,3], [5,6], [9,0]])
print(shoelace(shoe))
'''
'''
P6.2.2
'''



