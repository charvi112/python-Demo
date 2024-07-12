# implement a program that reads a json file into a pandas DataFrame and handles outlier using winsorization.
import pandas as pd
from scipy.stats.mstats import winsorize

def winsorize_data(df, limits):
    
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    for col in numeric_cols:
        df[col] = winsorize(df[col], limits=limits)
    return df


df = pd.read_json('C:\python\Day-14\data.json')  
print("Original DataFrame:")
print(df)

df_winsorized = winsorize_data(df, limits=(0.05, 0.05))
print("\nDataFrame after Winsorization:")
print(df_winsorized)
