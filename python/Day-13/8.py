# from csv file compare the sales data of different product using bar plot

import pandas as pd
import matplotlib.pyplot as plt

def create_bar_plot(data_file):
    try:
        df = pd.read_csv(data_file)
    except FileNotFoundError:
        print(f"Error: File '{data_file}' not found.")
        return
    
    if 'Product' not in df.columns or 'Sales' not in df.columns:
        print("Error: Required columns 'Product' and 'Sales' not found in the DataFrame.")
        return
    
    plt.figure(figsize=(10, 6))
    plt.bar(df['Product'], df['Sales'], color='skyblue')
    plt.xlabel('Product')
    plt.ylabel('Sales')
    plt.title('Sales Comparison of Different Products')
    plt.grid(axis='y')
    
    output_filename = 'product_sales_barplot.png'
    plt.savefig(output_filename)
    print(f"Bar plot saved as '{output_filename}'.")
    
    plt.show()

data_file = 'D:\course\Day_13_Practice_question\product_sales.csv'
create_bar_plot(data_file)
