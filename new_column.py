import pandas as pd

data = {
    "name": ["jateen", "kishaan", "pravin", "govind", "mukesh", "nirmala"],
    "age": [28, 37, 38, 29, 35, 38],
    "salary": [45000, 28000, 50000, 60000, 48000, 55000],
    "performance_score": [93.5, 89, 94, 83.8, 89, 95.5]
}

df = pd.DataFrame(data)
print(df)

# method 1: add new column
df["bonus"] = df["salary"] * 0.05
print("\n\n")
print(df)
print("\n\n")

# method 2: add new column using insert method
df.insert(0, "employee_id", [110,130,140,150,160,170])
print(df)

