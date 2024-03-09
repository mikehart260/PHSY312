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
plt.show()
plt.close(1)

'''
PLOT 2: Normal Mode Number with all spring constants
of 1 N/m and masses of 1kg
'''

plt.figure(2)
n = 30
frequencies, vec = myFunc(n,np.ones(n),np.ones(n+1))
plt.scatter(range(0,len(frequencies)), np.sort(frequencies))
plt.xlabel("Normal Mode Number")
plt.ylabel("Normal Mode Frequency (rad/s)")
plt.show()
plt.close(2)

'''
PLOT 3: Mass Index amplitudes at different frequencies with all spring constants
of 1 N/m and masses of 1kg
'''
plt.figure(3)
print(frequencies)

max_freq_idx = np.argmax(frequencies)
min_freq_idx = np.argmin(frequencies)

for mass_idx in range(0,n):
    if mass_idx < n-1:
        plt.scatter(mass_idx, vec[mass_idx][min_freq_idx], color='blue', marker='s')
        plt.scatter(mass_idx, vec[mass_idx][max_freq_idx], color='g', marker='.')
        plt.scatter(mass_idx, vec[mass_idx][n//2], color = 'orange', marker='+')
    else:
        plt.scatter(mass_idx, vec[mass_idx][min_freq_idx], color='blue', marker='s',label='lowest frequency')
        plt.scatter(mass_idx, vec[mass_idx][max_freq_idx], color='g', marker='.',label='highest frequency')
        plt.scatter(mass_idx, vec[mass_idx][n//2], color = 'orange', marker='+',label='middle frequency')

plt.ylabel('Amplitude')
plt.xlabel('Mass Index')
plt.legend()
plt.show()
plt.close(3)
'''
PLOT 4: Normal Mode Frequencies vs Number of Mases with spring constants multiples of 10 and masses of 1kg
'''
N = 50
k_s = [10*(x-1) for x in range(1,N+2)]
print(k_s)
plt.figure(4)
for n in range(2,N+1):
    freq,v = myFunc(n,np.ones(n),k_s)
    for w in freq:
        plt.scatter(n,w)

plt.xticks([10,20,30,40,50])
plt.ylabel('Normal Mode Frequency (radians)')
plt.xlabel('Number of Masses')
plt.title('k\'s = multiples of 10, all masses = 1 kg')
plt.show()
plt.close(4)

'''
PLOT 5: Normal Mode Number with all spring constants
of 1 N/m and masses of 1kg
'''
n = 30
plt.figure(5)
k_s = [2**x - 1 for x in range(1,n+2)]
print(k_s)
frequencies, vec = myFunc(n,np.ones(n),k_s)
plt.scatter(range(0,len(frequencies)), np.sort(frequencies))
plt.xlabel("Normal Mode Number")
plt.yscale('log')
plt.ylabel("Normal Mode Frequency (rad/s)")
plt.title("K's = 2^x -1, high spring constant = high frequency, log scale")
plt.show()
plt.close(5)