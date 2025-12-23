import pandas as pd

data1 = {
    'id': [1,2,3,4,5,6,7],
    'Department': ['HR', 'Sale', 'Finance', 'HR', 'Sale', 'Sale', 'HR']
}
data2 = {
    'emp_id': [1,2,3,4,5,6,7],
    'Salary': [25000, 20000, 35000, 30000, 22000, 19000, 25000]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

final = df1.merge(df2, left_on='id', right_on='emp_id')

print(final)