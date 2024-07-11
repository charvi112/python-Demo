# simple line plot using matplotlib

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 10, 5]

plt.figure(figsize=(8, 4))  
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Line 1') 
plt.title('Simple Line Plot')
plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')
plt.legend()  
plt.grid(True)  
plt.show()
