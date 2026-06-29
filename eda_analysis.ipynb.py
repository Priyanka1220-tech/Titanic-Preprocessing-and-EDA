# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create folders if they do not exist
os.makedirs('../images', exist_ok=True)
os.makedirs('../data', exist_ok=True)

# Load Dataset
df = pd.read_csv(r"C:\Users\Dell\Desktop\dod.csv")

# Inspect Dataset
print("First 5 Rows:")
print(df.head())

print("\nShape of Dataset:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

# Handle Missing Values
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
df['Cabin'] = df['Cabin'].fillna('Unknown')

# Remove Duplicate Rows
df = df.drop_duplicates()

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Summary Statistics
print("\nSummary Statistics:")
print(df.describe())

# Correlation Analysis
corr = df.corr(numeric_only=True)
print("\nCorrelation Matrix:")
print(corr)

# Visualization 1: Histogram
plt.figure(figsize=(6,5))
plt.hist(df['Age'], bins=20)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.savefig('../images/age_distribution.png')
plt.show()

# Visualization 2: Scatter Plot
plt.figure(figsize=(6,5))
plt.scatter(df['Age'], df['Fare'])
plt.title('Age vs Fare')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.savefig('../images/age_vs_fare.png')
plt.show()

# Visualization 3: Correlation Heatmap
plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.savefig('../images/correlation_matrix.png')
plt.show()

# Save Cleaned Dataset
df.to_csv('../data/cleaned_dataset.csv', index=False)

print("\nCleaned dataset saved as '../data/cleaned_dataset.csv'")
print("Images saved in '../images/' folder.")
