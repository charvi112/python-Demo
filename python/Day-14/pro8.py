import pandas as pd
from sklearn.preprocessing import StandardScaler
def standardize_data(df):

    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    return df


df = pd.read_csv('C:\python\Day-14\data.csv') 
print("Original DataFrame:")
print(df)

df_standardized = standardize_data(df)
print("\nDataFrame after Standardization:")
print(df_standardized)

