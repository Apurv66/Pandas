import pandas as pd

data = {
    "hours_studied": [2, 3, 4, 5, 6],
    "exam_score": [50, 60, 65, 70, 80],
    "sleep_hours": [7, 6, 6, 5, 5]
}

df = pd.DataFrame(data)

print(df.corr())