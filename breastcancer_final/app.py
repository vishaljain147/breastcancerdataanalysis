import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# Load dataset with correct encoding
df = pd.read_csv("breast_cancer_data.csv", encoding='utf-8-sig')

# Clean column names
df.columns = df.columns.str.strip().str.replace("\ufeff", "")

# Display first five rows
print(df.head())

# Display dataset shape
print("Dataset shape:", df.shape)

# Generate summary statistics
print(df.describe())
# Check for missing values
print("Missing values per column:\n", df.isnull().sum())

# Handle missing values
if 'Bare_Nuclei' in df.columns:
    df.loc[:, 'Bare_Nuclei'] = df['Bare_Nuclei'].fillna(df['Bare_Nuclei'].median())

# Convert Class column to numeric values safely
class_mapping = {'benign': 0, 'malignant': 1}
df['Class'] = df['Class'].astype(str).map(class_mapping)

# Normalize numerical columns (except Class)
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
if 'Class' in numeric_cols:
    numeric_cols.remove('Class')

# Fill missing values before scaling
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

# Apply Min-Max scaling
scaler = MinMaxScaler()
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

# Create new column safely
if 'Marginal_Adhesion' in df.columns and 'Clump_Thickness' in df.columns:
    df['Cell_Adhesion_Ratio'] = df['Marginal_Adhesion'] / (df['Clump_Thickness'] + 1e-9)

# Filter dataset for malignant cases
malignant_df = df[df['Class'] == 1]

# Compute mean values per class
print("Class-wise mean values:\n", df.groupby('Class').mean())

# Compute statistics
for col in ['Clump_Thickness', 'Cell_Size_Uniformity']:
    if col in df.columns:
        print(f"{col} - Mean: {np.mean(df[col])}, Median: {np.median(df[col])}, Std: {np.std(df[col])}")

# Correlation check
if 'Cell_Shape_Uniformity' in df.columns and 'Bland_Chromatin' in df.columns:
    correlation = df[['Cell_Shape_Uniformity', 'Bland_Chromatin']].corr()
    print("Correlation between Cell_Shape_Uniformity and Bland_Chromatin:\n", correlation)

# Top 3 correlated features with Class
top_corr = df.corr()['Class'].abs().sort_values(ascending=False)[1:4]
print("Top 3 most correlated features with Class:\n", top_corr)

# Malignant percentage
malignant_percentage = (df['Class'].sum() / len(df)) * 100
print(f"Percentage of malignant cases: {malignant_percentage:.2f}%")

# Quartile calculations
if 'Single_Epi_Cell_Size' in df.columns:
    q1, q3 = np.percentile(df['Single_Epi_Cell_Size'], [25, 75])
    iqr = q3 - q1
    print(f"Single_Epi_Cell_Size - Q1: {q1}, Q3: {q3}, IQR: {iqr}")

# Visualization
plt.hist(df['Clump_Thickness'], bins=10, alpha=0.7, color='blue')
plt.title('Histogram of Clump Thickness')
plt.xlabel('Clump Thickness')
plt.ylabel('Frequency')
plt.show()

df.boxplot(column='Cell_Size_Uniformity', by='Class', grid=False)
plt.title('Box plot of Cell Size Uniformity')
plt.suptitle('')
plt.xlabel('Class (0: Benign, 1: Malignant)')
plt.ylabel('Cell Size Uniformity')
plt.show()

plt.scatter(df['Bland_Chromatin'], df['Normal_Nucleoli'], c=df['Class'], cmap='coolwarm', alpha=0.7)
plt.xlabel('Bland Chromatin')
plt.ylabel('Normal Nucleoli')
plt.title('Scatter plot: Bland Chromatin vs Normal Nucleoli')
plt.colorbar(label='Class (0: Benign, 1: Malignant)')
plt.show()

plt.hist(df['Bare_Nuclei'], bins=10, alpha=0.7, color='green')
plt.title('Distribution of Bare Nuclei')
plt.xlabel('Bare Nuclei')
plt.ylabel('Frequency')
plt.show()

df.groupby('Class')['Mitoses'].mean().plot(kind='bar', color=['blue', 'red'])
plt.xticks(ticks=[0, 1], labels=['Benign', 'Malignant'], rotation=0)
plt.title('Average Mitoses Count for Benign and Malignant Cases')
plt.xlabel('Class')
plt.ylabel('Average Mitoses Count')
plt.show()
