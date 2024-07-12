import pandas as pd
import numpy as np

data = {
    'A': [1, 2, 3, 4],
    'B': [np.nan, 5, 6, np.nan],
    'C': ['a', 'b', np.nan, 'd']
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
df_cleaned = df.dropna()
print("\nDataFrame after removing missing values:")
print(df_cleaned)
