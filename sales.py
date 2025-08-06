# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset
try:
    # Load the dataset (Make sure to use raw string or double backslashes for Windows paths)
    df = pd.read_csv(r'C:\Users\USER\Downloads\zara.csv')
    print("✅ Dataset loaded successfully.")
except FileNotFoundError:
    print("❌ File not found. Please check the path and filename.")
    exit()

# Display first few rows
print("\n📌 First 5 rows of the dataset:")
print(df.head())

# Dataset info
print("\n📌 Dataset Info:")
print(df.info())

# Check for missing values
print("\n📌 Missing values in each column:")
print(df.isnull().sum())

# Clean the dataset - drop missing values
df_cleaned = df.dropna()
print("\n✅ Data after cleaning:")
print(df_cleaned.info())

# Task 2: Basic Data Analysis

# 1. Basic statistics
print("\n📊 Basic Statistics:")
print(df_cleaned.describe())

# 2. Median and Std Dev
print("\n📏 Median of numeric columns:")
print(df_cleaned.median(numeric_only=True))

print("\n📐 Standard Deviation of numeric columns:")
print(df_cleaned.std(numeric_only=True))

# 3. Grouping by a categorical column (assuming 'species' exists in the dataset)
if 'species' in df_cleaned.columns:
    grouped_means = df_cleaned.groupby('species').mean(numeric_only=True)
    print("\n📌 Mean values grouped by species:\n")
    print(grouped_means)

    print("\n🧠 Interesting Findings:")
    for column in grouped_means.columns:
        max_group = grouped_means[column].idxmax()
        max_value = grouped_means[column].max()
        print(f"- The species with the highest average {column} is {max_group} ({max_value:.2f})")
else:
    print("\n⚠️ Column 'species' not found for grouping.")
    grouped_means = None

# Task 3: Data Visualization

# Set Seaborn style
sns.set(style="whitegrid")

# 1. Line Chart (simulate trend using index vs petal_length)
if 'petal_length' in df_cleaned.columns:
    plt.figure(figsize=(10, 5))
    plt.plot(df_cleaned.index, df_cleaned['petal_length'], label='Petal Length')
    plt.title('Line Chart: Petal Length Over Index')
    plt.xlabel('Index')
    plt.ylabel('Petal Length')
    plt.legend()
    plt.tight_layout()
    plt.show()

# 2. Bar Chart (average petal_length per species)
if grouped_means is not None:
    grouped_means['petal_length'].plot(kind='bar', color='teal', edgecolor='black')
    plt.title('Bar Chart: Average Petal Length per Species')
    plt.xlabel('Species')
    plt.ylabel('Average Petal Length')
    plt.tight_layout()
    plt.show()

# 3. Histogram (Distribution of Sepal Width)
if 'sepal_width' in df_cleaned.columns:
    plt.figure(figsize=(8, 5))
    sns.histplot(df_cleaned['sepal_width'], kde=True, bins=15, color='orange')
    plt.title('Histogram: Distribution of Sepal Width')
    plt.xlabel('Sepal Width')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

# 4. Scatter Plot (Sepal Length vs Petal Length)
if 'sepal_length' in df_cleaned.columns and 'petal_length' in df_cleaned.columns:
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='sepal_length', y='petal_length', hue='species', data=df_cleaned)
    plt.title('Scatter Plot: Sepal Length vs Petal Length')
    plt.xlabel('Sepal Length')
    plt.ylabel('Petal Length')
    plt.tight_layout()
    plt.show()
