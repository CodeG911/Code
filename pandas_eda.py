import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('customer_transactions.csv')

# Handle missing values: fill with mean for 'transaction_amount'
df['transaction_amount'].fillna(df['transaction_amount'].mean(), inplace=True)

# Remove duplicates
df = df.drop_duplicates()

# Display basic summary statistics
print(df.describe())

# Visualizations
# Histogram for 'transaction_amount'
plt.figure(figsize=(8, 6))
sns.histplot(df['transaction_amount'], kde=True)
plt.title('Transaction Amount Distribution')
plt.show()

# Boxplot for 'transaction_amount'
plt.figure(figsize=(8, 6))
sns.boxplot(x=df['transaction_amount'])
plt.title('Boxplot of Transaction Amount')
plt.show()

# Correlation heatmap for numerical features
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
