import numpy as np
import matplotlib.pyplot as plt

def myFunc(n, masses, springs):
    '''
    Parameters:
    n (int): Number of atoms
    masses: Array containing masses of atoms
    springs: Array containing spring constants, with a size n+1
    
    Returns:
    array: eigenvalues, eigenvectors
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
    return frequencies, vectors

'''
PLOT 1: Normal Mode Frequencies vs Number of Mases with all spring constants
of 1 N/m and masses of 1kg
'''

plt.figure(1)
for n in range(2,31):
    freq,v = myFunc(n,np.ones(n),np.ones(n+1))
    for w in freq:
        plt.scatter(n,w)

plt.xticks([5,10,15,20,25,30])
plt.ylabel('Normal Mode Frequency (radians)')
plt.xlabel('Number of Masses')
plt.title('all k\'s = 1 N/m all masses = 1 kg')
plt.close(1)

'''
PLOT 2: Normal Mode Number
'''

plt.figure(2)
n = 30
frequencies, vec = myFunc(n,np.ones(n),np.ones(n+1))
plt.scatter(range(0,len(frequencies)), np.sort(frequencies))
plt.xlabel("Normal Mode Number")
plt.ylabel("Normal Mode Frequency (rad/s)")
# plt.show()
plt.close(2)

'''
PLOT 3: 
'''
plt.figure(3)
print(frequencies)

max_freq_idx = np.argmax(frequencies)
min_freq_idx = np.argmin(frequencies)

for mass_idx in range(0,n):
    plt.scatter(mass_idx, vec[max_freq_idx][mass_idx], color='g', marker='.')
    plt.scatter(mass_idx, vec[min_freq_idx][mass_idx], color='blue', marker='s')

plt.show()