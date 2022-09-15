import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

df1=pd.read_csv('mtcars.csv')
df2=pd.read_csv('pokemon.csv')
df3=pd.read_csv('housing_train.csv')
'''
mpg  - milhas/galão
cyl  - # cilindros
disp - Deslocamento
hp   - Horse Power - potência
draft- Relação do eixo traseiro
wt   - Peso
qsec - Tempo para percorer 1/4 milha
vs   - motor em v - 0 ou em linha - 1
am   - Transmissão 0 - automática 1 - manual 
gear - # marchas
carb - # carburadores
'''

#print(df1.head()) #Tabela dos carros
print(df2.head()) #Tabela dos pokemons

#sns.scatterplot(x='mpg', y='disp', data=df2);
#sns.scatterplot(x='attack', y='defense', data=df2); #ataque x defesa
#sns.lmplot(x='attack', y='defense', data=df2); #ataque x defesa com linha
#sns.scatterplot(x='attack', y='defense',data=df2, hue='is_legendary'); #ataque x defesa (lendario)
#sns.lmplot(x='attack', y='defense',data=df2, hue='is_legendary'); #ataque x defesa (lendario) com linha
#sns.scatterplot(x='attack', y='defense', data=df2, hue='type1'); #ataque x defesa (tipo)
#sns.scatterplot(x='weight_kg', y='height_m', data=df2[df2['type1'] == 'water']); #peso x altura (tipo = agua)
sns.distplot(df3.SalePrice);
plt.show()

#print(stats.pearsonr(df1['cyl'],df1['hp'])) #Mostra a correlação das colunas selecionadas
#mapa = df1.corr() # Mostra todas as correlações
#print(round(mapa,2))

# monte pelo menos 3 correlações distintas com ou sem agrupamento hue

'''
Para o dataset do pokemon monte e mostre as seguintes correlações

Correlação ataque x defesa

Correlação ataque x defesa agrupado po ser legendário ou não

Correlação ataque x defesa por tipo (type1)

Corelação peso x altura (weight_kg x height_m) só dos pokemons do tipo água (type1 = 'water')
'''