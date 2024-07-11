# create line plot to visualize the trend of a specific column 

import pandas as pd
import matplotlib.pyplot as plt

filename = 'D:\course\Day_13_Practice_question\data1.csv'  

try:
    df = pd.read_csv(filename)
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    exit()

# Step 2: Prepare data for plotting
df['Date'] = pd.to_datetime(df['Date'])  
x_variable = df['Date']
y_variable = df['Sales']

# Step 3: Plotting
plt.figure(figsize=(10, 6))  
plt.plot(x_variable, y_variable, marker='o', linestyle='-', color='blue', alpha=0.7)
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Line Plot of Sales Over Time')
plt.grid(True)

output_filename = 'line_plot.png'  
plt.savefig(output_filename)
print(f"Line plot saved as '{output_filename}'.")
plt.show()
