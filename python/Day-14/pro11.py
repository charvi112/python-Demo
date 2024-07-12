# given a csv file with customer details,preprocess the data for future analysis (e.g, handel missing values,scale features).
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

def preprocess_data(file_path):
    
    df = pd.read_csv(file_path)
    print("Original DataFrame:")
    print(df)
    
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    imputer = SimpleImputer(strategy='mean')
    df[numeric_cols] = imputer.fit_transform(df[numeric_cols])
    

    categorical_cols = df.select_dtypes(include=['object']).columns
    imputer = SimpleImputer(strategy='most_frequent')
    df[categorical_cols] = imputer.fit_transform(df[categorical_cols])
    
    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    
    print("\nPreprocessed DataFrame:")
    print(df)
    return df
file_path = 'C:\python\Day-14\data.csv' 
preprocessed_df = preprocess_data(file_path)
