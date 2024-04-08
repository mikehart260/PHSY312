import matplotlib.pyplot as plt
import numpy as np
# # x = range(4)
# # letters = 'ABCD'
# # lcount = {'A':10, 'B':15, 'C':20, 'D':25}
# # norm = sum(lcount.values())
# # fig, ax = plt.subplots()

# # ax.bar(x,[lcount[letter]/norm * 100 for letter in letters])
# ##################################################################

# data = {}

# bmi = np.genfromtxt('/Users/michaelhart/repos/PHSY312/pair/week_08/bmi_men.tsv',filling_values=-1,delimiter='\t',dtype=str)
# gdp = np.genfromtxt('/Users/michaelhart/repos/PHSY312/pair/week_08/gdp.tsv',filling_values=-1,delimiter='\t',dtype=str)
# pop = np.genfromtxt('/Users/michaelhart/repos/PHSY312/pair/week_08/population_total.tsv',filling_values=-1,delimiter='\t',dtype=str)

# for line in bmi:
#     data[line[0]] = [-1,-1,-1]
# for line in gdp:
#     data[line[0]] = [-1,-1,-1]
# for line in pop:
#     data[line[0]] = [-1,-1,-1]

# for line in bmi:
#     data[line[0]][0] = line[1]
# for line in gdp:
#     data[line[0]][1] = line[1]
# for line in pop:
#     data[line[0]][2] = line[1]

# for country in data.keys():
#     if float(data[country][0]) != -1 and float(data[country][1]) != -1 and float(data[country][2]) != -1:
#         plt.scatter(float(data[country][0]),float(data[country][1]),s=int(data[country][2])/100000,label=country)

# plt.xlabel("BMI")
# plt.ylabel("GDP")

# plt.show()




# fig, ax = plt.subplots()

# ax.scatter(bmi, gdp, s=pop)
# plt.show()


# 7.5.4
c = -0.1 + 0.65j
# n x n 
n = 200
z_max = 10

grid = np.zeros((n,n))

real = np.linspace(-1.5,1.5,n)
imag = np.linspace(-1.5j, 1.5j, n)
count_max = 500

for i_idx,i in enumerate(real):
    for j_idx,j in enumerate(imag):
        z = i + j
        count = 0
        while np.abs(z) < z_max:
            z = z**2 + c
            count += 1
            if count >= count_max:
                break
        
        grid[i_idx][j_idx] = count

fig, ax = plt.subplots()
im = ax.pcolormesh(grid)        
plt.show() 
