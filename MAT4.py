import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('population-figures-by-country-csv_csv.csv', index_col=0)
del data['Country_Code']
data = data.T
ire_croatia = data[['Ireland', 'Croatia']].reset_index()
print(ire_croatia)

fig,ax = plt.subplots(figsize=(14,8))
x = ire_croatia['index']
y = ire_croatia['Ireland']
y2 = ire_croatia['Croatia']

ax.plot(x, y, color='green')
ax.plot(y2, color='red')

plt.xticks(rotation='vertical')
ax.set_xticks(x[::5])
plt.ylabel('People (Millions)', rotation='horizontal')
plt.title('Population of Ireland & Croatia 1960 - 2016')

plt.show()
