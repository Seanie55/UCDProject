import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('week 25OWGR.csv')
data1 = data[0:50]
countrygroup = data1.groupby(['Ctry']).count()
sortgroup = countrygroup.sort_values('Player Id', ascending=False).reset_index()
print(sortgroup)

fig,ax = plt.subplots(figsize=(14,8))
y = sortgroup['Player Id']
labels = ['USA', 'ENG', 'AUS', 'RSA','ESP', 'KOR', 'CAN', 'CHI', 'FRA', 'IRL', 'JPN', 'MEX', 'NIR', 'NOR', 'SCO']
ax.pie(y, labels = labels, autopct= '%.0f%%')

plt.title('Country Split of Top 50 Ranked Golfers')

plt.show()