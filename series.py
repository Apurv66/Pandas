import pandas as pd
import numpy as np

# create series from list
a = pd.Series([1,2,3,4])
print(a)

# create own label or index
b = pd.Series([1,2,3,4], index=['a','b','c','d'])
print(b)

# create series from dictionary
c = pd.Series({'a':10, 'b':20, 'c':30})
print(c)

# create series from numpy array
d = np.array([1,2,3,4])
e = pd.Series(d)
print(e)