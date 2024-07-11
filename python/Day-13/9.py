# read json file into pandas and use seaborn to create violin plot

import pandas as pd
import seaborn as sns
import json
import matplotlib.pyplot as plt

def read_json_file(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            df = pd.DataFrame(data)
            return df
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: '{filename}' is not a valid JSON file.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def create_violin_plot(df, column_name):
    if df is None:
        return
    
    try:
        sns.violinplot(data=df, x=column_name)
        plt.title(f'Violin Plot of {column_name}')
        plt.show()
    except Exception as e:
        print(f"An error occurred while creating the violin plot: {e}")
    finally:
        plt.close()
        
    print("Violin plot created successfully.")
    
filename = "data.json"

df = read_json_file(filename)

if df is not None:
    column_name = input("Enter the column name to create the violin plot: ")
    create_violin_plot(df, column_name)
