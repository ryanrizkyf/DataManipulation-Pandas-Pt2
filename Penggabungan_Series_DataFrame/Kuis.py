import pandas as pd
df1 = pd.DataFrame({
    'key': ['k1', 'k2', 'k3', 'k4', 'k5'],
    'val1': [200, 500, 0, 500, 100],
    'val2': [30, 50, 100, 20, 10],

})
df2 = pd.DataFrame({
    'key': ['k1', 'k1', 'k5', 'k7', 'k10'],
    'val3': [1, 2, 3, 4, 5],
    'val4': [6, 7, 8, 8, 10]
})
pd.merge(df1, df2, validate="1:1")
