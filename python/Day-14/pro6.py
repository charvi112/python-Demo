# crete a function that takes a pandas DataFrame and converts text data into numerical values using pandas one-Hot Encoding.

import pandas as pd
def one_hot_encode(df):

    
    df_encoded = pd.get_dummies(df, drop_first=True)
    return df_encoded

data = {
    'color': ['red', 'blue', 'green', 'orange', 'purple'],
    'size': ['S', 'M', 'L', 'M', 'S']
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

df_encoded = one_hot_encode(df)
print("\nDataFrame after One-Hot Encoding:")
print(df_encoded)
