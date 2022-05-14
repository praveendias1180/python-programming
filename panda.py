import pandas as pd

data = {"calories": [420, 380, 390], "duration": [50, 40, 45]}
print(data)

# load data into a DataFrame object:
df = pd.DataFrame(data)

print(df)

df = pd.read_csv("pandadata.csv")
print(df.to_string())