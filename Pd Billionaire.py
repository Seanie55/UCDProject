import pandas as pd

file = 'forbes_billionaires_geo.csv'
data = pd.read_csv(file, index_col=4)

missing_values = data.isnull().sum()
dropcols = data.dropna(axis=1)
drop_dup = data.drop_duplicates(subset=['Name'])
top_10 = data.iloc[0:10, 0:5]
average_age = top_10['Age'].mean()
Top_age = top_10['Age'].max()

print("Average Age of Top 10 is: ", (average_age))
print("Max Age of Top 10 is: ", (Top_age))



