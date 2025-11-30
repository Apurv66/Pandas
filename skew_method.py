import pandas as pd

data = {
    "customer_age": [21, 25, 30, 32, 40, 45, 52, 70],
    "monthly_spending": [120, 180, 250, 300, 400, 500, 750, 1100],
    "product_rating": [4.6, 4.4, 4.2, 4.0, 3.8, 3.5, 3.0, 2.8]
}

df = pd.DataFrame(data)

print(df.skew())