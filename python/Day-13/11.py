import pandas as pd
import matplotlib.pyplot as plt

def create_pie_chart(df, column):

    data = df[column].value_counts()

    plt.figure(figsize=(8, 8))
    plt.pie(data, labels=data.index, autopct='%1.1f%%', startangle=140)
    plt.title(f'Distribution of {column}')
    plt.axis('equal') 

    plt.show()


if __name__ == "__main__":

    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 28, 35, 27],
        'Gender': ['Female', 'Male', 'Male', 'Female', 'Female']
    }
    df = pd.DataFrame(data)
    
    create_pie_chart(df, 'Gender')
