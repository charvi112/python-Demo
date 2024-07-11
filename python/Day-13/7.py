# using pandas create a box plot to visualize the distribution of the data

import pandas as pd
import matplotlib.pyplot as plt

def create_box_plot(data_file, column_name):
    try:
        df = pd.read_csv(data_file)
    except FileNotFoundError:
        print(f"Error: File '{data_file}' not found.")
        return
    
    if column_name not in df.columns:
        print(f"Error: Column '{column_name}' not found in the DataFrame.")
        return
    
    df.boxplot(column=column_name)
    
    plt.savefig(f"{column_name}_boxplot.png")
    
    print(f"Box plot saved as '{column_name}_boxplot.png'")
    
    plt.show()

data_file = "D:\course\Day_13_Practice_question\data3.csv"
column_name = "salary"

create_box_plot(data_file, column_name)
