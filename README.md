# 📊 Data Analysis & Visualization Report: Iris Dataset

## 🔍 Task 1: Data Loading and Exploration
- The Iris dataset was loaded using `sklearn.datasets.load_iris()` and converted to a pandas DataFrame.
- It contains 150 samples with 4 numerical features:
  - Sepal Length (cm)
  - Sepal Width (cm)
  - Petal Length (cm)
  - Petal Width (cm)
- The dataset also includes a categorical column: `species` (setosa, versicolor, virginica).
- No missing values were found in the dataset.

---

## 📈 Task 2: Basic Data Analysis
- The `.describe()` summary shows that petal length and width vary significantly across species.
- Sepal length has the highest mean (~5.84 cm).
- Grouping by species revealed:
  - **Setosa** has the smallest petal length.
  - **Virginica** has the largest.
  - **Versicolor** lies in between.

---

## 🖼 Task 3: Visualizations

### 1. Line Chart:
- Simulated cumulative sepal length shows a steady increase across the dataset.

### 2. Bar Chart:
- Average petal length by species:
  - Setosa: ~1.46 cm
  - Versicolor: ~4.26 cm
  - Virginica: ~5.55 cm

### 3. Histogram:
- Sepal length is right-skewed, with most values between 5.0–6.0 cm.

### 4. Scatter Plot:
- Shows strong separation between species based on sepal and petal length.
- Setosa forms a distinct cluster with small values.

---

## 🧠 Observations
- Petal length is a strong indicator of species.
- The dataset is balanced, clean, and ideal for classification tasks.
- Visualizations clearly show how species differ in key flower measurements.
