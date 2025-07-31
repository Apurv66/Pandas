import pandas as pd

data = {
    "name": ["jateen", "kishaan", "pravin", "govind", "mukesh", "nirmala"],
    "age": [28, None, 38, 29, 35, 38],
    "salary": [45000, None, 50000, 60000, 48000, 55000],
    "performance_score": [93.5, None, 94, 83.8, 89, 95.5]
}

df = pd.DataFrame(data)
print(df)

# drop column or row which have missing value
"""
df.dropna(inplace=True)
print(df)
"""

# fill the missing value
df.fillna(0, inplace=True)
print(df)

