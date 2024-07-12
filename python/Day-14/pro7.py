# Given pandas dataframe,normalize the numeric features using Z-score Normalization.

import pandas as pd
from sklearn.preprocessing import StandardScaler

def z_score_normalization(df):
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns

    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    return df

data = {
    'Name': ['raj', 'diya', 'chirag', 'kuldeep', 'nishi'],
    'Age': [32, 30, 22, 28, 25],
    'Salary': [35000, 14000, 29000, 15000, 3000]
}

df = pd.DataFrame(data)
normalized_df = z_score_normalization(df)

print("Normalized DataFrame:")
print(normalized_df)


