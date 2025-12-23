import pandas as pd

data = {
    "name":['arun','karun','varun'],
    "age":[28,36,33],
    "salary":[36000,60000,45000]
}

df = pd.DataFrame(data)
df.sort_values(by="age", ascending=True, inplace=True)
print(df)