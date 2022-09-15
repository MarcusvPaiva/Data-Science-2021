import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("imports-85.csv")
# como o dataset vem sem cabeçalho, vamos colocar um cabeçalho nele
headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style", "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type", "num-of-cylinders", "engine-size","fuel-system", "bore", "stroke", "compression-ratio", "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price"]
df.columns = headers
#print(df.head(5))

# como os simbolos de ? não nos são uteis, vamos trocar pela representação de nulo do numpy
df = df.replace('?',np.NaN)
#print(df.head(5))

# podemos verificar quais colunas possuem valores nulos na nossa base
#missing_data = df.isnull()
#print(missing_data.head(5))

# quantos dados faltantes possui cada coluna ?
'''
for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")
'''
# o que fazemos com as linhas que possuem valorse nulos ??
# Opção 1 - Apagar estas linhas
# Opção 2 - Gerar dados para subistituir os valores faltantes

# Vamos com a opção 2 aqui !
# Vamos utilizar os valores médios das colunas que possuem dados para isto
avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)  # calcula a média dos valores da coluna
df["normalized-losses"].replace(np.nan, avg_norm_loss, inplace=True)  # realiza a substituição

avg_bore = df['bore'].astype('float').mean(axis=0)
df["bore"].replace(np.nan, avg_bore, inplace=True)

avg_stroke = df['stroke'].astype('float').mean(axis=0)
df["stroke"].replace(np.nan, avg_stroke, inplace=True)

avg_horsepower = df['horsepower'].astype('float').mean(axis=0)
df['horsepower'].replace(np.nan, avg_horsepower, inplace=True)

avg_peakrpm = df['peak-rpm'].astype('float').mean(axis=0)
df['peak-rpm'].replace(np.nan, avg_peakrpm, inplace=True)

avg_price = df['price'].astype('float').mean(axis=0)
df['price'].replace(np.nan, avg_price, inplace=True)

df["num-of-doors"].replace(np.nan, "four", inplace=True)

# este segundo passo corrige os tipos de dados que o pandas interpreta errado

df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["normalized-losses", "horsepower"]] = df[["normalized-losses", "horsepower"]].astype("int")
df[["price"]] = df[["price"]].astype("float")
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")

#print(df)
#print(df.dtypes)

var1 = 'lenght'
var2 = 'width'
var3 = 'horsepower'
var4 = 'peak-rpm'
var5 = 'highway-mpg'
var6 = 'city-mpg'
#Para calcular a correlação de Pearson entre duas variáveis
#pearson_coef, p_value = stats.pearsonr(df[var1], df[var2]) Positivo
#pearson_coef, p_value = stats.pearsonr(df[var3], df[var4]) zero
pearson_coef, p_value = stats.pearsonr(df[var5], df[var6])
print("A correlação de Pearson para as variaveis '"+var5+"' e '"+var6+"' é :", pearson_coef)

# para plotar um gráfico de disperção
#sns.regplot(x=var1, y=var2, data=df)
#sns.regplot(x=var3, y=var4, data=df)
sns.regplot(x=var5, y=var6, data=df)
plt.show()

#print(df.corr())

#print(df.dtypes)
#Pos(+) = lenght x width (0,84), curb-weight x engine-size(0,85), city-mpg x highway-mpg (0,97), 
#Pos(+) = 
#Zero(0) = horsepower x peak-rpm (0,13), bore x stroke (-0,05), 
#Symboling x ''(1)(+)
# '' x normalized-losses(0,47)(+)
# '' x wheel-base(-0,52)(-)*
# '' x length(-0,35)(-)
# '' x width (-0,23)(-)
# '' x curb-weight (-0,23)(-)
# '' x engine-size (-0,11)(-)
# '' x bore (-0,14)(-)
# '' x stroke (0,01)(0)
# '' x compression-ratio (-0,17)(-)
# '' x horsepower (0,07)(0)
# '' x peak-rpm (0,27)(+)
# '' x city-mpg
# '' x highway-mpg
# '' x price
#compression-ratio x normalized-losses(-0,11)(-)
# '' x wheel-base(0,25)(+)
# '' x length(0,15)(+)
# '' x width(0,18)(+)
# '' x height(0,26)(+)
# '' x curb-weight(0,15)(+)
# '' x engine-size(0,02)(0)
# '' x bore(0,00)(0)*
# '' x stroke(0,18)(+)
# '' x '' (1)(+)
# '' x horsepower(-0,20)(-)
# '' x peak-rpm(-0.43)(-)
# '' x city-mpg(0,32)(+)
# '' x highway-mpg(0,26)(+)
# '' x price (0,07)(0)