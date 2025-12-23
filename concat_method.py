import pandas as pd

df_refion1 = pd.DataFrame({
    'customer_id': [1,2],
    'name': ['vikash', 'varun']    
})

df_refion2 = pd.DataFrame({
    'customer_id': [3,4],
    'name': ['shyam', 'suresh']    
})

df_concat = pd.concat([df_refion1, df_refion2], axis=0, ignore_index=True)

print(df_concat)