import pandas as pd

df = pd.DataFrame({
    "Age": [10, 20, 30, 40],
    "Salary": [1000, 2000, 3000, 4000]
})

def double(x):
    return x * 2

df["Age_doubled"] = df["Age"].apply(double)

print(df)
