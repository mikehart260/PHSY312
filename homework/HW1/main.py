import math
import numpy as np
import matplotlib.pyplot as plt

def binomial_coefficient(n,k):
    # integer division works here.
    return math.factorial(n)//(math.factorial(k)*math.factorial(n-k))

def coin_prob(n,k):
    return binomial_coefficient(n,k)/(2**n)

def flip(n):
    rng = np.random.default_rng()
    heads = 0
    for i in range(n):
        if (rng.random() < 0.5):
            heads+=1
    return heads

NUM_FLIPS = 100
probs = []

print("P = {:.9f}".format(coin_prob(1500,800)))
count = 0
for i in range(NUM_FLIPS):
    x = coin_prob(NUM_FLIPS,i)
    probs.append(x) # this helps me find the ymax for vline
    plt.plot(i, x, 'ko')
    if i == NUM_FLIPS - 1:
        # set the label for the legend on the last point only
        plt.plot(i, x, 'ko', label = "prediction")

actual = flip(NUM_FLIPS)

plt.vlines(actual, 0, max(probs),label = f"actual = {actual}")
plt.legend()
plt.xlabel("Num of heads")
plt.ylabel("Probability")

plt.show()