import matplotlib.pyplot as plt

x = range(4)
letters = 'ABCD'
lcount = {'A':10, 'B':15, 'C':20, 'D':25}
norm = sum(lcount.values())
fig, ax = plt.subplots()




ax.bar(x,[lcount[letter]/norm * 100 for letter in letters])
ax.set_xticks
