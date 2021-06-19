import pandas as pd

file = 'forbes_billionaires_geo.csv'
data = pd.read_csv(file, index_col=0)
top50 = data[0:50]

for name, country in top50.iterrows():
        print(name + ":" + str(country['Country'].upper()))


