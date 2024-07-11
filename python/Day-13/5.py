# histogram to visualize the distribution of data

import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read CSV file into a pandas DataFrame
filename = 'D:\course\Day_13_Practice_question\data1.csv'  # Replace with your CSV file path
try:
    df = pd.read_csv(filename)
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    exit()

# Step 2: Prepare data for plotting
# Use the 'Sales' column for the histogram
sales_data = df['Sales']

# Step 3: Plotting
plt.figure(figsize=(10, 6))  # Adjust figure size as needed
plt.hist(sales_data, bins=5, color='blue', alpha=0.7)  # Adjust number of bins as needed
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.title('Histogram of Sales')
plt.grid(True)

# Step 4: Show and save the plot as an image file
output_filename = 'histogram.png'  # Replace with your desired output file name
plt.savefig(output_filename)
print(f"Histogram saved as '{output_filename}'.")
plt.show()
