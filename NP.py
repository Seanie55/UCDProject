import numpy as np

file1 = 'week24 OWGR.csv'

data1 = np.loadtxt(file1, delimiter=',', dtype=str, usecols=8,  skiprows=1)
data2 = np.loadtxt(file1, delimiter=',', dtype=str, usecols=9,  skiprows=1)
TotalptsT100 = (data1[0:100,])
EventsplayedT100 = (data2[0:100,])
ar1 = np.array(TotalptsT100.astype(np.float64))
ar2 = np.array(EventsplayedT100.astype(np.int64))
average_points = ar1 / ar2
print("Top 100 golfers World Ranking by Average Points: ", average_points)


