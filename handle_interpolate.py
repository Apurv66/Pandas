import pandas as pd

data = {
    "time":[1,2,3,4,5],
    "value":[10, None, 30, None, 50]
}

df = pd.DataFrame(data)
print(df)

df['value'] = df['value'].interpolate(method="time")
print(df)