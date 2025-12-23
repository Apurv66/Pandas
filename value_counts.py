import pandas as pd

data = {
    'id': [1,2,3,4,5,6,7,8],
    'Result': ['Pass', 'Pass', 'Fail', 'Pass', 'Pass', 'Fail', 'Fail', 'Pass']
}

df = pd.DataFrame(data)

print(df['Result'].value_counts())