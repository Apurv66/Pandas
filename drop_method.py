import pandas as pd

data = {
    "name": ["jateen", "kishaan", "pravin", "govind", "mukesh", "nirmala"],
    "age": [28, 37, 38, 29, 35, 38],
    "salary": [45000, 28000, 50000, 60000, 48000, 55000],
    "performance_score": [93.5, 89, 94, 83.8, 89, 95.5]
}

df = pd.DataFrame(data)
print(df)
print('\n')

df.drop(columns=['performance_score', 'age'], inplace=True)
print(df)