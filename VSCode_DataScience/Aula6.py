import pandas as pd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import numpy as np

fig, ax1 = plt.subplots()
'''
# Covariância
matematica = [84, 82, 81, 89, 73, 94, 92, 70, 88, 95]
fisica = [85, 82, 72, 77, 75, 89, 95, 84, 77, 94]
portugues = [97, 94, 93, 95, 88, 82, 78, 84, 69, 78]

data = np.array([matematica, fisica, portugues])

print("Matriz de covariância:\n", np.cov(data))

# Correlação de Person
independente = [10,20,40,45,60,65,75,80]

#dependente = [100,10,130,90,40,80,180,50]
#dependente = [40,40,60,80,90,110,100,130]
dependente = [32,44,68,74,92,98,110,116]

ax1.plot(independente, dependente, "bo")
plt.show()

df = pd.read_csv("mtcars.csv")
 
# Convert dataframe into series
list1 = df['qsec']
list2 = df['hp']
 
# Apply the pearsonr()
corr, _ = pearsonr(list1, list2)
print('Correlação de Pearsons: %.3f' % corr)
'''
df = pd.read_csv("anscombe.csv")

list1 = df['x4']
list2 = df['y4']
 
corr, _ = pearsonr(list1, list2)
print('Correlação de Pearsons: %.3f' % corr)

ax1.plot(list1, list2, "bo")
plt.show()
#'''