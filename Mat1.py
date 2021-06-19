import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('forbes_billionaires_geo.csv')
countrygroup = data.groupby(['Country']).sum()
sortgroup = countrygroup.sort_values('NetWorth', ascending=False).reset_index()
print(sortgroup[0:10])
fig,ax = plt.subplots(figsize=(14,8))
x = sortgroup['Country'].head(10)
y = sortgroup['NetWorth'].head(10)

ax.bar(x,y)
plt.xlabel('Country')
plt.ylabel('Networth')
plt.title('Top 10 Countries by Networth')
plt.yticks([0,500,1000,1500,2000,2500,3000,3500,4000,4500,5000],
    ['0B','500B','1000B','1500B','2000B','2500B','3000B','3500B','4000B','4500B','5000B'])
plt.setp(ax.get_xticklabels(), rotation = 35)

plt.show()