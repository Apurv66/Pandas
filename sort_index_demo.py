import pandas as pd

data = {
    'id': [4,3,2,1,5],
    'name': ['ramesh', 'suresh', 'chirag', 'rajesh', 'karan']
}

df = pd.DataFrame(data)

df.set_index('id', inplace=True)
print(df)

df.sort_index(inplace=True)
print(df)