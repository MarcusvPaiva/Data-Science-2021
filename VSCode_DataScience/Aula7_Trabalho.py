import pandas as pd  
import numpy as np  
import sklearn 
from sklearn.linear_model import LinearRegression
from sklearn import metrics as mt
import seaborn as sns 
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt 
from sklearn import datasets

diabetes = datasets.load_diabetes()

db_df = pd.DataFrame(diabetes.data,columns=diabetes.feature_names)
'''
Codigo do trabalho a partir da linha 30
'''
#print(diabetes.DESCR)

#print(db_df.head())

# Cria uma coluna chamada Progressão (Variável dependente)
db_df['Progressao'] = diabetes.target
#print(db_df.head())

#Cria um dataset com todas a variáveis independentes
x = db_df.drop(labels='Progressao', axis=1)
# Cria um dataset com a variável dependente
y = db_df['Progressao']

#Quebra o dataset em treino e teste
#Usar outros tamanhos de test size
#Escolha das colunas
# Colunas presentes na tabela: age, sex, bmi, bp, s1, s2, s3, s4, s5, s6
x1 = db_df['age'].to_numpy().reshape(-1, 1)
y1 = db_df['sex'].to_numpy().reshape(-1, 1)
x2 = db_df['bmi'].to_numpy().reshape(-1, 1)
y2 = db_df['bp'].to_numpy().reshape(-1, 1)
x3 = db_df['s1'].to_numpy().reshape(-1, 1)
y3 = db_df['s2'].to_numpy().reshape(-1, 1)
x4 = db_df['s3'].to_numpy().reshape(-1, 1)
y4 = db_df['s4'].to_numpy().reshape(-1, 1)

#Configuração do teste e treino
train_x1, test_x1, train_y1, test_y1 = train_test_split(x1,y1,test_size=0.3,random_state=999) #x1 e y1 
train_x2, test_x2, train_y2, test_y2 = train_test_split(x2,y2,test_size=0.1,random_state=999) #x2 e y2
train_x3, test_x3, train_y3, test_y3 = train_test_split(x3,y3,test_size=0.7,random_state=999) #x3 e y3
train_x4, test_x4, train_y4, test_y4 = train_test_split(x4,y4,test_size=0.8,random_state=999) #x4 e y4
lm = LinearRegression()
#predicted_y = lm.predict(test_x)
#Configuração dos gráficos
#1º Gráfico = compara age e sex com tamanho do teste 0,3
plt.title('Regressão linear com treino - 1º Gráfico (tamanho 0,3)')
lm.fit(train_x1, train_y1)
plt.scatter(test_x1, test_y1, color='blue', edgecolors='black', label='age x sex') #mostra os pontos do gráfico em azul
plt.plot(test_x1, lm.predict(test_x1), color='green', label='Regressão Linear') #linha de regressão (verde em todos os gráficos)
plt.legend()
plt.show()
#2º Gráfico = compara bmi e bp com tamanho do teste 0,1
lm.fit(train_x2, train_y2)
plt.title('Regressão linear com treino - 2º Gráfico (tamanho 0,1)')
plt.scatter(test_x2, test_y2, color='yellow', edgecolors='black', label='bmi x bp') #mostra os pontos do gráfico em amarelo
plt.plot(test_x2, lm.predict(test_x2), color='green', label='Regressão Linear')
plt.legend()
plt.show()
#3º Gráfico = compara s1 e s2 com tamanho do teste 0,7
lm.fit(train_x3, train_y3)
plt.title('Regressão linear com treino - 3º Gráfico (tamanho 0,7')
plt.scatter(test_x3, test_y3, color='orange', edgecolors='black', label='s1 x s2') #mostra os pontos do gráfico em laranja
plt.plot(test_x3, lm.predict(test_x3), color='green', label='Regressão Linear')
plt.legend()
plt.show()
#4º Gráfico = compara s3 e s4 com tamanho do teste 0,8
lm.fit(train_x4, train_y4)
plt.title('Regressão linear com treino - 4º Gráfico (tamanho 0,8)')
plt.scatter(test_x4, test_y4, color='red', edgecolors='black', label='s3 x s4') #mostra os pontos do gráfico em vermelho
plt.plot(test_x4, lm.predict(test_x4), color='green', label='Regressão Linear')
plt.legend()
plt.show()

#print(predicted_y)