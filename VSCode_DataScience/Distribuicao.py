import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('./housing_train.csv')
print(data.head)
plt.hist(data.SalePrice)
plt.show()

import seaborn as sns
sns.distplot(data.SalePrice);
plt.show()

sns.distplot(data.SalePrice.head(100))
plt.show()

sns.distplot(data.SalePrice.head(1000))
plt.show()