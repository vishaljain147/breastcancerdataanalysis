🔬 Breast Cancer Data Analysis
This project performs data cleaning, preprocessing, statistical analysis, and visualization on a breast cancer dataset. The goal is to identify key patterns that differentiate benign and malignant cases.

📂 Dataset
Ensure the dataset file breast_cancer_data.csv is present in the project directory.

Column Name	Description
Clump_Thickness	Thickness of cell clumps
Cell_Size_Uniformity	Uniformity of cell size
Cell_Shape_Uniformity	Uniformity of cell shape
Bare_Nuclei	Number of bare nuclei in cells
Bland_Chromatin	Texture of cell chromatin
Mitoses	Number of mitotic cells (cell division activity)
Class	0 = Benign, 1 = Malignant
⚙️ Setup & Installation
1️⃣ Install Dependencies
Make sure you have Python installed, then install required libraries:

pip install pandas numpy matplotlib scikit-learn
2️⃣ Run the Script
Execute the script using:

python main.py
📊 Features & Functionality
✅ Data Cleaning & Preprocessing

Removes unnecessary characters from column names
Handles missing values using median imputation
Converts categorical labels to numerical values (0 = benign, 1 = malignant)
Normalizes numerical columns using MinMax Scaling
✅ Statistical Analysis

Calculates mean, median, standard deviation of key features
Finds top 3 correlated features with malignancy
Computes the percentage of malignant cases
✅ Visualizations
📌 Histogram of Clump Thickness
📌 Box Plot of Cell Size Uniformity (Benign vs Malignant)
📌 Scatter Plot: Bland Chromatin vs Normal Nucleoli
📌 Bar Chart: Mitoses Count by Class

📊 Sample Output

Dataset shape: (699, 11)
Missing values per column:
Bare_Nuclei    2
...
Percentage of malignant cases: 35.46%
Top 3 most correlated features with Class:
1. Cell_Size_Uniformity: 0.72
2. Bare_Nuclei: 0.67
3. Bland_Chromatin: 0.65
🔹 Next Steps
Add Machine Learning models to classify benign vs malignant cases
Optimize feature selection for better insights
Compare different normalization techniques
📜 License
This project is licensed under the MIT License.
