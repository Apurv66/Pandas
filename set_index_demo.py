import pandas as pd

data = {
    'id': [1,2,3,4,5],
    'name': ['ramesh', 'suresh', 'chirag', 'rajesh', 'karan']
}

df = pd.DataFrame(data)

df.set_index('id', inplace=True)
print(df)