import numpy as np

M = np.array([[1,0,-1,0,0],[3,-1,-2,0,0],[2,1,-1,0,0],[3,1,-2,-2,0],[2,1,-2,0,-1]])
x = [1,1,1,1,1]

M_inv = np.linalg.inv(M)
print(M_inv)