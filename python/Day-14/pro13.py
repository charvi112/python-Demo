# implement a function that takes pandas Dataframe and performs data discretization on a numeric feature.
import pandas as pd
def discretize_feature(df, feature, bins, labels=None):
    df[f'{feature}_binned'] = pd.cut(df[feature], bins=bins, labels=labels)
    return df
data = {
    'age': [18,28,25,34,39,28,40,48,55,68,70]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
df_discretized = discretize_feature(df, 'age', bins=3, labels=["Young", "Middle-aged", "Old"])

print("\nDataFrame after Discretization:")
print(df_discretized)
