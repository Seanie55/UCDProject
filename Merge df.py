import pandas as pd
golfrankw24 = pd.read_csv('week24 OWGR.csv')
golfrankw25 = pd.read_csv('week 25OWGR.csv')
cleanwk24 = golfrankw24.fillna(0)
cleanwk25 = golfrankw25.fillna(0)
concat_data = pd.concat([cleanwk25, cleanwk24])
join_data = cleanwk25.join(cleanwk24,lsuffix="WK25", rsuffix="WK24")
merged_data = pd.merge(cleanwk25, cleanwk24, on='Player Id')
print(cleanwk25.shape, cleanwk24.shape)
print(concat_data.shape, join_data.shape, merged_data.shape)
print(join_data.info())




