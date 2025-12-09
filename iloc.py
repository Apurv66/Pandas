import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Esha'],
    'age': [23, 29, 31, 22, 27],
    'gender': ['F', 'M', 'M', 'M', 'F'],
    'department': ['Electrical', 'Computer', 'Computer', 'Electrical', 'Medical'],
    'salary': [45000, 52000, 48000, 50000, 47000],
    'city': ['New York', 'Chicago', 'Boston', 'Houston', 'Seattle']
}


df = pd.DataFrame(data)

print(df.iloc[:, 2]) # Select a single column by index

print(df.iloc[:, 1:4])

print(df.iloc[:, [0,3,5]]) # Selecting specific index values (use a list)

