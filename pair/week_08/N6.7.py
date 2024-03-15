import numpy as np

def chain(N,Vp):
    M = np.zeros((N,N))

    for i in range(N):
        if i == 0:
            M[i][0] = 3
            M[i][1] = -1
            M[i][2] = -1
        elif i == N-1:
            M[i][i-2] = -1
            M[i][i-1] = -1
            M[i][i]= 3
        else: 
            M[i][i] = 4
            if (i - 2 < 0):
                M[i][i-1] = -1
            else:
                M[i][i-1] = -1
                M[i][i-2] = -1
            
            if (i + 2 > N-1):
                M[i][i+1] = -1
            else: 
                M[i][i+1] = -1
                M[i][i+2] = -1
    
    w = np.zeros(N)
    w[0] = Vp
    w[1] = Vp
    v = np.linalg.solve(M,w)
    return v

print(chain(10000,5))