# importando pacotes
from math import sqrt
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sct
import seaborn as sns

'''
fig, ax = plt.subplots(1, 3, figsize=(15, 4))
fig.subplots_adjust(wspace=0.1)

np.random.seed(50)

#gera uma amostra ed 100000 núneros aleatórios, forçando a distribuição
pop_normal = sct.norm.rvs(loc = 2000, scale = 200,  size=100000)
pop_exp = sct.expon.rvs(scale = 2000, size=100000)
pop_uniform = sct.uniform.rvs(loc = 1000, scale = 2000, size=100000)


sns.distplot(pop_normal, bins=20, hist_kws={"density": True}, ax=ax[0])
ax[0].set_title('Distribuição Normal', fontsize=14)
ax[0].set_xlabel('Valor médio da distribuição = {}'.format(pop_normal.mean().round(2)), fontsize = 12)
ax[0].set_yticks([])
sns.distplot(pop_exp,  bins=20, hist_kws={"density": True}, ax=ax[1])
ax[1].set_title('Distribuição Exponencial', fontsize=14)
ax[1].set_xlabel('Valor médio da distribuição = {}'.format(pop_exp.mean().round(2)), fontsize = 12)
ax[1].set_yticks([])
sns.distplot(pop_uniform, bins=20, hist_kws={"density": True}, ax=ax[2])
ax[2].set_title('Distribuição Uniforme', fontsize=14)
ax[2].set_xlabel('Valor médio da distribuição = {}'.format(pop_uniform.mean().round(2)), fontsize = 12)
ax[2].set_yticks([])

plt.show()

# Retiradas 1000 amostras, cada uma delas composta de 10, 30 e 50 elementos

# função para coleta das amostras aleatórias das distribuições
def get_sample(df, col_name, n, seed=42):    
    np.random.seed(seed)    
    random_idx = np.random.choice(df[col_name].dropna().index, size=n, replace=False)    
    return df.loc[random_idx, col_name]



# organizando médias amostrais
pops = pd.DataFrame({ 'normal' : pop_normal,
                     'exponencial' : pop_exp,
                     'uniforme' : pop_uniform})

dists = ['normal','exponencial','uniforme']
medias_df = pd.DataFrame({'numero_medias' : range(1000)})
tamanho_amostras = [10, 30, 50]
reps = medias_df.shape[0]

for dist in dists:
  for n in tamanho_amostras:
    medias = []
    for rep in range(reps):
      value = get_sample(pops, dist, n = n, seed = 42 + rep).mean()
      medias.append(value)
    medias_df['n:{}_d:{}'.format(n,dist)] = medias

#print(medias_df.head())

# mostrando os gráficos das distribuições populacionais e das médias amostrais
fig, ax = plt.subplots(3, 4, figsize=(20, 14))
fig.subplots_adjust(hspace=0.3, wspace=0.1)

sns.distplot(pops['normal'], bins=20, hist_kws={"density": True}, ax=ax[0,0])
ax[0,0].set_title('Distribuição Normal', fontsize=14)
ax[0,0].set_xlabel('Valor médio da distribuição = {}'.format(round(pops['normal'].mean(),2)), fontsize = 12)
ax[0,0].set_yticks([])

sns.distplot(medias_df['n:10_d:normal'], bins=20, hist_kws={"density": True}, ax=ax[0,1])
ax[0,1].set_title('Distribuição das médias - n = 10', fontsize=14)
ax[0,1].set_xlabel('Valor médio da distribuição = {}'.format(round(medias_df['n:10_d:normal'].mean(),2)), fontsize = 12)
ax[0,1].set_yticks([])

sns.distplot(medias_df['n:30_d:normal'], bins=20, hist_kws={"density": True}, ax=ax[0,2])
ax[0,2].set_title('Distribuição das médias - n = 30', fontsize=14)
ax[0,2].set_xlabel('Valor médio da distribuição = {}'.format(round(medias_df['n:30_d:normal'].mean(),2)), fontsize = 12)
ax[0,2].set_yticks([])

sns.distplot(medias_df['n:50_d:normal'], bins=20, hist_kws={"density": True}, ax=ax[0,3])
ax[0,3].set_title('Distribuição das médias - n = 50', fontsize=14)
ax[0,3].set_xlabel('Valor médio da distribuição = {}'.format(round(medias_df['n:50_d:normal'].mean(),2)), fontsize = 12)
ax[0,3].set_yticks([])


sns.distplot(pops['exponencial'], bins=20, hist_kws={"density": True}, ax=ax[1,0])
ax[1,0].set_title('Distribuição Exponencial', fontsize=14)
ax[1,0].set_xlabel('Valor médio da distribuição = {}'.format(round(pops['exponencial'].mean(),2)), fontsize = 12)
ax[1,0].set_yticks([])

sns.distplot(medias_df['n:10_d:exponencial'], bins=20, hist_kws={"density": True}, ax=ax[1,1])
ax[1,1].set_title('Distribuição das médias - n = 10', fontsize=14)
ax[1,1].set_xlabel('Valor médio da distribuição = {}'.format(round(medias_df['n:10_d:exponencial'].mean(),2)), fontsize = 12)
ax[1,1].set_yticks([])

sns.distplot(medias_df['n:30_d:exponencial'], bins=20, hist_kws={"density": True}, ax=ax[1,2])
ax[1,2].set_title('Distribuição das médias - n = 30', fontsize=14)
ax[1,2].set_xlabel('Valor médio da distribuição = {}'.format(round(medias_df['n:30_d:exponencial'].mean(),2)), fontsize = 12)
ax[1,2].set_yticks([])

sns.distplot(medias_df['n:50_d:exponencial'], bins=20, hist_kws={"density": True}, ax=ax[1,3])
ax[1,3].set_title('Distribuição das médias - n = 50', fontsize=14)
ax[1,3].set_xlabel('Valor médio da distribuição = {}'.format(round(medias_df['n:50_d:exponencial'].mean(),2)), fontsize = 12)
ax[1,3].set_yticks([])

sns.distplot(pops['uniforme'], bins=20, hist_kws={"density": True}, ax=ax[2,0])
ax[2,0].set_title('Distribuição Uniforme', fontsize=14)
ax[2,0].set_xlabel('Valor médio da distribuição = {}'.format(round(pops['uniforme'].mean(),2)), fontsize = 12)
ax[2,0].set_yticks([])

sns.distplot(medias_df['n:10_d:uniforme'], bins=20, hist_kws={"density": True}, ax=ax[2,1])
ax[2,1].set_title('Distribuição das médias - n = 10', fontsize=14)
ax[2,1].set_xlabel('Valor médio da distribuição = {}'.format(round(medias_df['n:10_d:uniforme'].mean(),2)), fontsize = 12)
ax[2,1].set_yticks([])

sns.distplot(medias_df['n:30_d:uniforme'], bins=20, hist_kws={"density": True}, ax=ax[2,2])
ax[2,2].set_title('Distribuição das médias - n = 30', fontsize=14)
ax[2,2].set_xlabel('Valor médio da distribuição = {}'.format(round(medias_df['n:30_d:uniforme'].mean(),2)), fontsize = 12)
ax[2,2].set_yticks([])

sns.distplot(medias_df['n:50_d:uniforme'], bins=20, hist_kws={"density": True}, ax=ax[2,3])
ax[2,3].set_title('Distribuição das médias - n = 50', fontsize=14)
ax[2,3].set_xlabel('Valor médio da distribuição = {}'.format(round(medias_df['n:50_d:uniforme'].mean(),2)), fontsize = 12)
ax[2,3].set_yticks([])

plt.show()


# importando a base de dados
df = pd.read_csv('DataScience.csv')

# observando os cinco primeiros valores
print(df.head())

#Tratar valores nulos
print(df["('P16', 'salary_range')"].isna().sum())  # mostra total e valores para um campo que são nulos

# Reescreve o DataFrame sem os valores Nulos
df.dropna(axis = 0, subset = ["('P16', 'salary_range')"], inplace = True)

# mantendo na amostra somente os profissionais que trabalham como cientistas de dados
df = df[df["('P19', 'is_data_science_professional')"] == 1]

print(df.head())

print(df["('P16', 'salary_range')"].unique())


# criando uma nova coluna com o valor médio do range de salários
df['salario'] = df["('P16', 'salary_range')"].map({'Menos de R$ 1.000/mês': 800,
                                                         'de R$ 1.001/mês a R$ 2.000/mês': 1500, 
                                                         'de R$ 2.001/mês a R$ 3000/mês': 2500,
                                                         'de R$ 3.001/mês a R$ 4.000/mês': 3500,
                                                         'de R$ 4.001/mês a R$ 6.000/mês': 5000,
                                                         'de R$ 6.001/mês a R$ 8.000/mês': 7000,
                                                         'de R$ 8.001/mês a R$ 12.000/mês': 10000,
                                                         'de R$ 12.001/mês a R$ 16.000/mês': 14000,
                                                         'de R$ 16.001/mês a R$ 20.000/mês': 18000,
                                                         'de R$ 20.001/mês a R$ 25.000/mês': 22500,
                                                         'Acima de R$ 25.001/mês': 25000})

print(df[["('P16', 'salary_range')", "salario"]].head())




# obtendo as estatísticas da variável alvo
print(df['salario'].describe())

# teste de hipótese para a variável alvo. H0: 19900
stat, p = sct.ttest_1samp(df['salario'], popmean=19900)
print('Estatística de teste: {}'.format(stat.round(2)))
print('p-valor: {}'.format(p.round(2)))


'''
