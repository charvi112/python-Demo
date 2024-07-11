# scatter plots using matplotlib to visualize relationships between two variables
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read CSV file into a pandas DataFrame
filename = 'D:\course\Day_13_Practice_question\data.csv'  # Replace with your CSV file path
try:
    df = pd.read_csv(filename)
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    exit()

# Step 2: Prepare data for plotting
x_variable = df['X Variable']
y_variable = df['Y Variable']

# Step 3: Plotting
plt.figure(figsize=(10, 6))  # Adjust figure size as needed
plt.scatter(x_variable, y_variable, color='blue', alpha=0.7)  # Adjust alpha for transparency
plt.xlabel('X Variable')
plt.ylabel('Y Variable')
plt.title('Scatter Plot of X Variable vs Y Variable')
plt.grid(True)

# Step 4: Show and save the plot as an image file
output_filename = 'scatter_plot.png'  # Replace with your desired output file name
plt.savefig(output_filename)
print(f"Scatter plot saved as '{output_filename}'.")
plt.show()
