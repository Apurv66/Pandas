import pandas as pd
import requests

res = requests.get("https://dummyjson.com/products")

df = pd.DataFrame(res.json()['products'])