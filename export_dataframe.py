import pandas as pd

data = {
    "name":["virat", "rohit","dhoni"],
    "runs":[4002,3403,2889],
    "average":[51.23, 42.83, 49.33],
    "strike_rate":[139, 149, 154]
}

df = pd.DataFrame(data)
print(df)

# df.to_csv("output.csv", index=False)
# df.to_excel("output.xlsx", index=False)
df.to_json("output.json", index=False)