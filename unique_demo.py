import pandas as pd

data = {
    'roll_no': [1,2,3,4,5,6],
    'department': ['computer', 'electrical', 'computer', 'civil', 'mechenical', 'mechenical']
}

df = pd.DataFrame(data)

print(df['department'].unique())
