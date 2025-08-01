import pandas as pd

df_customer = pd.DataFrame({
    'id': [1,2,3],
    'name': ['ramesh', 'suresh', 'kalpesh']
})

df_orders = pd.DataFrame({
    'id': [1,2,4],
    'orderAmount': [250,450,500]
})

# there are 4 type of join inner, outer, left and right
df_merged = pd.merge(df_customer, df_orders, on="id", how="inner")

print(df_merged)