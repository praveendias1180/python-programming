import pandas as pd
import numpy as np

data = {"calories": [420, 380, 390], "duration": [50, 40, 45]}
# print(data)

# load data into a DataFrame object:
df = pd.DataFrame(data)

# print(df)

df = pd.read_csv("pandadata.csv")
# print(df.to_string())

print(df.head(3))

print('......')
print(df.dropna())

print('......')
print(df.fillna(88))

print('......')
print(df.drop_duplicates())


print('------------------')
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print(s['a'])

a = np.array([1,2,3]) 
print(a)