import pandas as pd

df = pd.DataFrame({
    'date': ['2024-3-22', '22-3-2024', '2023-11-5', '5-11-2023']
})

# This converts multiple date formats in a column into one single consistent format (DD-MM-YYYY)
df['date'] = pd.to_datetime(df['date'], format='mixed').dt.strftime('%d-%m-%Y')

print(df)
