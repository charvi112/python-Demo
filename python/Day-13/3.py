# bar plot using seaborn and compare categorial variables

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Load the dataset
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 28, 35, 27],
    'Gender': ['Female', 'Male', 'Male', 'Female', 'Female']
})

# Step 2: Create a bar plot
sns.barplot(x='Gender', y='Age', data=df)

# Step 3: Set labels and title
plt.xlabel('Gender')
plt.ylabel('Age')
plt.title('Bar plot of Gender vs Age')

# Step 4: Save the plot
plt.savefig('bar_plot.png')

# Step 5: Show the plot
plt.show()
