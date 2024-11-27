import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Create a sample dataset 
data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Sales': [150, 200, 300, 250, 400],
    'Category': ['A', 'B', 'A', 'B', 'A']
})

# Plot a Line Graph (Trend over time)
plt.figure(figsize=(8, 5))
plt.plot(data['Month'], data['Sales'], marker='o', linestyle='-', color='b')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()

# Plot a Bar Chart (Comparing categories)
plt.figure(figsize=(8, 5))
sns.barplot(x='Month', y='Sales', hue='Category', data=data)
plt.title('Sales by Category per Month')
plt.show()

# Plot a Histogram (Frequency distribution of sales)
plt.figure(figsize=(8, 5))
sns.histplot(data['Sales'], bins=5, kde=True)
plt.title('Distribution of Sales')
plt.xlabel('Sales')
plt.show()
