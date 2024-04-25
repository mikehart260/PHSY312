# Q8.4.1 Q8.4.2 N6.16

# reading newman 6.3.5

import numpy as np
import scipy.optimize as optimize

def f(x):
    return (-1/(x-3)**3) - 1

sol = optimize.brentq(f,0,4)
print(sol)