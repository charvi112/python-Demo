#  write a python program that uses Scikit -learn to perform data trasformation using PCA(principal component analysis).
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def perform_pca(file_path, n_components=2):

    df = pd.read_csv(file_path)
    X = df.select_dtypes(include=['float64', 'int64'])
    X_scaled = StandardScaler().fit_transform(X)
    pca = PCA(n_components=n_components)
    X_pca = pca.fit_transform(X_scaled)
    pca_columns = [f'PC{i+1}' for i in range(n_components)]
    df_pca = pd.DataFrame(X_pca, columns=pca_columns)

    print("\nPCA Transformed DataFrame:")
    print(df_pca)
    return df_pca

file_path = 'C:\python\Day-14\data.csv'  
pca_df = perform_pca(file_path, n_components=2)
