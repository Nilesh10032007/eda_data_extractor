# Advanced EDA & Feature Engineering 🚀

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-green)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.2%2B-orange)

## 📌 Project Overview
This project demonstrates an industry-standard pipeline for Exploratory Data Analysis (EDA) and Feature Engineering on an e-commerce dataset. It is designed with modularity, clean code practices (PEP-8), and robustness in mind, making it suitable for production environments.

The pipeline performs intelligent missing value imputation, outlier handling, categorical encoding, and creates new engineered features to enhance predictive modeling.

## 📊 Dataset
The dataset `ecommerce_sales.csv` contains transactional data from an e-commerce platform. It includes features like:
- **Numerical:** `Quantity`, `UnitPrice`, `ItemsInCart`
- **Categorical:** `Product`, `PaymentMethod`, `OrderStatus`, `ReferralSource`
- **Datetime:** `Date`

## 🛠️ Data Preprocessing & Cleaning
### 1. Missing Value Handling
Missing values are handled intelligently based on their prevalence in each feature:
- **< 5% Missing:** Rows are dropped to avoid unnecessary bias.
- **5% - 20% Missing:** Imputed using the **Median** to handle skewed distributions.
- **> 20% Missing:** Imputed using **KNN Imputation** (K-Nearest Neighbors) to leverage the relationships between features.

### 2. Outlier Detection & Handling
Outliers are detected using the **IQR (Interquartile Range)** method. 
- **Action:** Winsorization. Instead of removing data points and losing valuable information, outliers are capped at the lower and upper bounds.

## 🧬 Feature Engineering
Three new meaningful features were engineered to capture business logic:
1. **Time Features:** `OrderDayOfWeek`, `OrderHour`, and `IsWeekend` to capture seasonality and purchasing behavior over time.
2. **Cart Metrics:** `AvgItemValueInCart` (TotalPrice / ItemsInCart) to measure average spending per item.
3. **Customer Loyalty:** `CustomerOrderCount` to capture how many times a customer has purchased.

### Categorical Encoding & Multicollinearity
- **One-Hot Encoding:** Applied to low-cardinality categorical features (e.g., `PaymentMethod`, `OrderStatus`).
- **Multicollinearity Check:** A correlation matrix is evaluated. Any features with a Pearson correlation coefficient > **0.85** are removed to prevent model instability.

## 📁 Folder Structure
```text
project/
│
├── data/
│   ├── raw/                 # Original generated dataset
│   └── processed/           # Final cleaned dataset
│
├── notebooks/
│   └── EDA_and_Feature_Engineering.ipynb  # Beginner-friendly walkthrough
│
├── src/                     # Modular Python codebase
│   ├── config.py            # Paths and parameters
│   ├── preprocessing.py     # Missing values & outliers logic
│   ├── feature_engineering.py # Feature creation & encoding
│   ├── visualization.py     # Plotting utilities
│   └── generate_data.py     # Script to generate raw data
│
├── outputs/                 # Saved visualizations (PNGs)
├── main.py                  # Entry point to run the pipeline
├── README.md                # Project documentation
└── requirements.txt         # Dependencies
```

## 🚀 Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd Advanced-EDA-Feature-Engineering
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Data Generation (Optional):**
   ```bash
   python src/generate_data.py
   ```

4. **Execute the Pipeline:**
   ```bash
   python main.py
   ```

5. **Explore the Notebook:**
   Open Jupyter Notebook or JupyterLab to explore the interactive analysis.
   ```bash
   jupyter notebook notebooks/EDA_and_Feature_Engineering.ipynb
   ```

## 📈 Visualizations
The `outputs/` folder contains generated visual assets:
- `missing_values.png`
- `histograms.png`
- `boxplots.png`
- `correlation_heatmap.png`

---
*Built with ❤️ *
