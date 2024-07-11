import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def generate_pairplot(df):
    sns.pairplot(df)
    plt.show()

if __name__ == "__main__":
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': [2, 3, 4, 5, 6],
        'D': [5, 3, 1, 2, 4]
    }
    df = pd.DataFrame(data)
    
    generate_pairplot(df)
