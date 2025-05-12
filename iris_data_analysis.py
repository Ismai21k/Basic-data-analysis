
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Error handling for loading the dataset
try:
    # Load Iris dataset
    iris_data = load_iris()
    df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
    df['species'] = pd.Categorical.from_codes(iris_data.target, iris_data.target_names)

    print("First 5 rows of the dataset:")
    print(df.head())

    print("\nDataset info:")
    print(df.info())

    print("\nChecking for missing values:")
    print(df.isnull().sum())

    # Basic Data Analysis
    print("\nBasic statistics:")
    print(df.describe())

    print("\nAverage petal length by species:")
    group_mean = df.groupby("species")["petal length (cm)"].mean()
    print(group_mean)

    # Visualizations

    # 1. Line chart: simulate trend (cumulative sum of sepal length)
    df['cumulative_sepal_length'] = df['sepal length (cm)'].cumsum()
    plt.figure(figsize=(8, 5))
    plt.plot(df.index, df['cumulative_sepal_length'], label='Cumulative Sepal Length')
    plt.title("Line Chart: Cumulative Sepal Length Over Samples")
    plt.xlabel("Sample Index")
    plt.ylabel("Cumulative Sepal Length (cm)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # 2. Bar chart: average petal length by species
    plt.figure(figsize=(6, 4))
    group_mean.plot(kind='bar', color=['skyblue', 'salmon', 'limegreen'])
    plt.title("Bar Chart: Average Petal Length by Species")
    plt.xlabel("Species")
    plt.ylabel("Average Petal Length (cm)")
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

    # 3. Histogram: sepal length distribution
    plt.figure(figsize=(6, 4))
    plt.hist(df['sepal length (cm)'], bins=20, color='orange', edgecolor='black')
    plt.title("Histogram: Sepal Length Distribution")
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

    # 4. Scatter plot: sepal length vs petal length
    plt.figure(figsize=(6, 4))
    sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species')
    plt.title("Scatter Plot: Sepal Length vs Petal Length")
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Petal Length (cm)")
    plt.legend(title='Species')
    plt.tight_layout()
    plt.show()

except Exception as e:
    print(f"An error occurred: {e}")
