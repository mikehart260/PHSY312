import numpy as np
import matplotlib.pyplot as plt

def myFunc(n, masses, springs):
    '''
    Parameters:
    n (int): Number of atoms
    masses: Array containing masses of atoms
    springs: Array containing spring constants, with a size n+1
    
    Returns:
    array: eigenvalues
    '''
    K = np.zeros((n,n)) # initialize matrix

    # Build Matrix K
    for row in range(n):
        for col in range(n):
            if row == col:
                K[row,col] = springs[row] + springs[row+1]
            elif col == row+1: 
                K[row,col] = -springs[row+1]
            elif col == row-1:
                K[row,col] = -springs[row]

    # values = mw^2
    values,vectors = np.linalg.eig(K)
    
    # get frequencies
    frequencies = np.sqrt(values/masses)
    return frequencies

'''
PLOT 1: Normal Mode Frequencies vs Number of Mases with all spring constants of 1 N/m and masses of 1kg
'''
plt.figure(1)
for n in range(2,31):
    for w in myFunc(n,np.ones(n),np.ones(n+1)):
        plt.scatter(n,w)

plt.xticks([5,10,15,20,25,30])
plt.ylabel('Normal Mode Frequency (radians)')
plt.xlabel('Number of Masses')
plt.title('all k\'s = 1 N/m all masses = 1 kg')
plt.close(1)

'''
PLOT 2: 
'''
plt.figure(2)
n = 30
frequencies = myFunc(n,np.ones(n),np.ones(n+1))
for i,f in enumerate(frequencies):
    plt.scatter(i,f)

plt.show()
plt.close(2)

