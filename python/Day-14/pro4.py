# given a pandas dataframe,remove duplicate row and reset the index of the DataFrame.

import pandas as pd

data = {'Name': ['Raj', 'chitra', 'jiya', 'riya', 'jay'],
        'Age': [22, 30, 27, 32, 30],
        'City': ['Ahmedabad', 'Gandhinagar', 'sanad', 'Ahmedabad', 'baroda']}

df = pd.DataFrame(data)
df.drop_duplicates(inplace=True)
df.reset_index(drop=True, inplace=True)
print(df) 



