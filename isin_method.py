import pandas as pd

data = {
    'id': [1,2,3,4,5,6,7],
    'Department': ['HR', 'Sale', 'Finance', 'HR', 'Sale', 'Sale', 'HR']
}
df = pd.DataFrame(data)

print(df[df['Department'].isin(['HR', 'Finance'])])