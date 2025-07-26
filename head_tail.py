import pandas as pd

df = pd.read_csv("test.csv")

print("first 10 rows:\n", df.head(10))

print("last 10 rows:\n", df.tail(10))

print("first 10 rows:\n", df.head()) # by default it is 5 rows

print("last 10 rows:\n", df.tail()) # by default it is 5 rows

