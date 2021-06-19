import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('population-figures-by-country-csv_csv.csv', index_col=0)
del data['Country_Code']
data = data.T
ire = data['Ireland'].reset_index()
print(ire)

fig,ax = plt.subplots(figsize=(14,8))
x = ire['index']
y = ire['Ireland']

ax.scatter(x, y, color='green')
ax.set_xticks(x[::5])
plt.xticks(rotation='vertical')
plt.ylabel('People (Millions)', rotation='horizontal')
plt.title('Population of Ireland 1960 - 2016')
plt.show()
