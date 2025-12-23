import pandas as pd

data = {
    'Product': ['Phone', 'Laptop', 'Phone', 'Headphone', 'Mouse', 'Keyboard', 'Headphone', 'Mouse'],
    'Month': ['Dec', 'Dec', 'Nov', 'Dec', 'Dec', 'Dec', 'Nov', 'Nov'],
    'Sales': [20000, 55000, 30000, 2500, 1200, 2000, 3000, 1500]
}
df = pd.DataFrame(data)

pivot = pd.pivot_table(df, values='Sales', index='Month', columns='Product', aggfunc='sum', fill_value=0)

print(pivot)