import pandas as pd

data = {
    'Con': ['Ind', 'Sa', 'Aus', 'Nz', 'Eng']
}

df = pd.DataFrame(data)

df = df.rename(columns={'Con':'Country'})

print(df)