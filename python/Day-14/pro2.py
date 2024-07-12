# convert categorical variables into numerical values using  label Encoding

import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = {
    'color': ['red', 'blue', 'green', 'purple', 'orange'],
    'size': ['S', 'M', 'L', 'M', 'S']
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

label_encoder = LabelEncoder()
df['color_encoded'] = label_encoder.fit_transform(df['color'])
df['size_encoded'] = label_encoder.fit_transform(df['size'])
print("\nDataFrame after Label Encoding:")
print(df)
