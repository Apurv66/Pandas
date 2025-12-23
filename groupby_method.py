import pandas as pd

data = {
    "name": ['arun', 'karun', 'varun', 'mohit', 'umesh', 'suresh', 'navin', 'vinay', 'pravin'],
    "age": [28, 36, 33, 35, 39, 42, 46, 29, 28],
    "salary": [36000, 60000, 45000, 48000, 63000, 60000, 55000, 28000, 31000],
    "city": ["ahemadabad", "mahesana", "ahemadabad", "patan", "gandinagar", "gandinagar", "mahesana", "patan", "gandinagar"]
}

df = pd.DataFrame(data)

ans = df.groupby("city")["salary"].sum() # we can perform all aggregation functions
print(ans)
