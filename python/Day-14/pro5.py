# implement a program that reades a csv file into a pandas  dataframe and handles missing values using imputation.

import pandas as pd
from sklearn.impute import SimpleImputer

df = pd.read_csv(r'C:\python\Day-14\data.csv')
print("Original DataFrame:")
print(df)
imputer = SimpleImputer(strategy='mean')

numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
df[numeric_cols] = imputer.fit_transform(df[numeric_cols])
print("\nDataFrame after Imputation:")
print(df)
