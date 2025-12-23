import pandas as pd

data = {
    "name":['arun','karun','varun'],
    "age":[28,36,33],
    "salary":[36000,60000,45000]
}

df = pd.DataFrame(data)

print(df['salary'].max())
print(df['salary'].min())
print(df['salary'].sum())
print(df['salary'].mean())