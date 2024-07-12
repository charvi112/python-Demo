#create a function that takes a pandas DataFrame and removes irrelevant features using features selection techniques.
import pandas as pd
from sklearn.feature_selection import SelectKBest, f_classif

def select_features(df, target_column, k):
    X = df.drop(columns=[target_column])
    y = df[target_column]
    
    selector = SelectKBest(score_func=f_classif, k=k)
    X_new = selector.fit_transform(X, y)
    
    selected_features = X.columns[selector.get_support()]
    
    df_selected = pd.DataFrame(X_new, columns=selected_features)
    df_selected[target_column] = y.values
    
    return df_selected
data = {
    'feature1': [1, 2, 3, 4, 5],
    'feature2': [10, 20, 30, 40, 50],
    'feature3': [100, 200, 300, 400, 500],
     'target': [0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

df_selected = select_features(df, target_column='target', k=3)

print("\nDataFrame after Feature Selection:")
print(df_selected)
