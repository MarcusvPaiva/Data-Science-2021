# pip install vega_datasets
# pip install sklearn
from vega_datasets import data
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler

df = data.cars()
print(df.head())
print(df.info())

#Elimina linhas com valores null
df.dropna(subset=['Horsepower', 'Miles_per_Gallon'], inplace=True)
# Ordena o DataSet
df.sort_values(by='Horsepower', inplace=True)
# Normaliza os dados
X = df['Horsepower'].to_numpy().reshape(-1, 1)
y = df['Miles_per_Gallon'].to_numpy().reshape(-1, 1)

plt.scatter(X, y, color='green', edgecolors='black', label='Potência x Consumo')
plt.legend()
plt.show()

#Cria e treina o modelo
linear_regressor = LinearRegression()
linear_regressor.fit(X, y)

# Mostra o gráfico com a regressão linear
plt.scatter(X, y, color='green', edgecolors='black', label='Potência x Consumo')
plt.plot(X, linear_regressor.predict(X), color='orange', label='Regressão Linear')
plt.title('Regressão Linear')
plt.legend()
plt.show()

# Mostra o gráfico com a regressão polinomial
poly_reg = PolynomialFeatures(degree = 2)
X_poly = poly_reg.fit_transform(X)
poly_reg_model = LinearRegression()
poly_reg_model.fit(X_poly, y)

plt.scatter(X, y, color='green', edgecolors='black', label='Potência x Consumo')
plt.plot(X, poly_reg_model.predict(X_poly), color='orange', label='Regressão Polinomial')
plt.title('Regressão Polinomial')
plt.legend()
plt.show()