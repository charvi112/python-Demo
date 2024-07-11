# generate heatmap using seaborn to visualize the correlation between variables

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

filename = 'D:\course\Day_13_Practice_question\data5.csv' 
try:
    df = pd.read_csv(filename)
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    exit()

correlation_matrix = df.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()

