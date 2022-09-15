import numpy as np
from sklearn.preprocessing import normalize
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
'''
v = np.random.rand(10)
print(v)
normalized_v = v/np.linalg.norm(v)
print(normalized_v)

normalized_v = normalize(v[:,np.newaxis], axis=0)
print(normalized_v)
'''
df = pd.read_csv('loan_data.csv')

print(df.head())

#Lendo apenas algumas colunas do DataSet
cols = ['int.rate', 'installment']
df = pd.read_csv('loan_data.csv', usecols = cols)

print(df.head())

#Padronização
scaler = StandardScaler() 
df_scaled = scaler.fit_transform(df)

print("Padronizado")
print(df_scaled)

#Normalização
scaler = MinMaxScaler() 
df_norm= scaler.fit_transform(df)

print("Normalizado")
print(df_norm)