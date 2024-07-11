# using seaborn create a scatter plot matrix for multiple variable in a data frame 

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Read CSV file into a pandas DataFrame
filename = 'D:\course\Day_13_Practice_question\data2.csv'  
try:
    df = pd.read_csv(filename)
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    exit()

# Step 2: Prepare data for plotting
df.drop(columns=['Date'], inplace=True)

# Step 3: Plotting
sns.pairplot(df)
plt.suptitle('Scatter Plot Matrix for Multiple Variables', y=1.02)  
plt.show()
