import numpy as np

file = 'forbes_billionaires_geo.csv'

data = np.loadtxt(file, delimiter=',', dtype=str, usecols=(0,1,2,3,4,5,), skiprows=1)
Top_10networth = np.array(data[0:10,1])
Maxage = np.array(data[0:50, 5])
Maxage[Maxage == ''] = 0
cvt1 = Top_10networth.astype(np.float64)
cvt2 = Maxage.astype(np.int64)

print("Total Networth in Top 10: ", np.sum(cvt1))
print("Oldest age in Top 50:", np.max(cvt2))
print("Median age in Top 50:", np.median(cvt2))