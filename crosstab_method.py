import pandas as pd

data = {
    "customer_age_group": ["18 to 25", "18 to 25", "26 to 35", "26 to 35", "36 to 50", "36 to 50", "50+", "50+"],
    "product_category": ["Electronics", "Clothing", "Electronics", "Groceries", "Clothing", "Groceries", "Electronics", "Clothing"]
}

df = pd.DataFrame(data)

print(pd.crosstab(df["customer_age_group"], df["product_category"]))
