import nbformat as nbf
import os

def create_notebook():
    nb = nbf.v4.new_notebook()
    
    # Title and Intro
    nb.cells.append(nbf.v4.new_markdown_cell("# Advanced EDA & Feature Engineering\n\nThis notebook demonstrates a complete, production-ready pipeline for Exploratory Data Analysis and Feature Engineering."))
    
    # Imports
    code_imports = """import pandas as pd
import numpy as np
import sys
import os

# Add src to path
sys.path.append(os.path.abspath('../'))

from src.preprocessing import DataPreprocessor
from src.feature_engineering import FeatureEngineer
from src.visualization import Visualizer
from src.config import RAW_DATA_PATH, OUTPUTS_DIR

import warnings
warnings.filterwarnings('ignore')"""
    nb.cells.append(nbf.v4.new_code_cell(code_imports))
    
    # Load Data
    nb.cells.append(nbf.v4.new_markdown_cell("## 1. Data Loading\nLet's load our raw e-commerce dataset."))
    code_load = """df = pd.read_csv(RAW_DATA_PATH)
df.head()"""
    nb.cells.append(nbf.v4.new_code_cell(code_load))
    
    # Initial Visualization (Raw Data)
    nb.cells.append(nbf.v4.new_markdown_cell("## 2. Initial Exploratory Data Analysis (EDA)\nVisualizing missing values, distributions, and outliers before preprocessing."))
    code_viz_raw = """vis = Visualizer(df, OUTPUTS_DIR)
vis.plot_missing_values()
vis.plot_histograms()
vis.plot_boxplots()
print("Plots have been saved to the 'outputs/' directory.")"""
    nb.cells.append(nbf.v4.new_code_cell(code_viz_raw))
    
    # Preprocessing
    nb.cells.append(nbf.v4.new_markdown_cell("## 3. Preprocessing (Missing Values & Outliers)\n- **<5% Missing:** Dropped\n- **5-20% Missing:** Median Imputed\n- **>20% Missing:** KNN Imputed\n- **Outliers:** Detected using IQR and winsorized."))
    code_preprocess = """preprocessor = DataPreprocessor(df)
df_clean = preprocessor.handle_missing_values()
df_clean = preprocessor.detect_and_handle_outliers(method='iqr', action='winsorize')
df_clean.head()"""
    nb.cells.append(nbf.v4.new_code_cell(code_preprocess))
    
    # Feature Engineering
    nb.cells.append(nbf.v4.new_markdown_cell("## 4. Feature Engineering\nCreating meaningful features (e.g., IsWeekend, CustomerOrderCount), encoding categoricals, and removing multicollinearity."))
    code_fe = """engineer = FeatureEngineer(df_clean)
df_featured = engineer.engineer_features()
df_featured = engineer.encode_categorical_features()
df_final = engineer.check_multicollinearity(threshold=0.85)
df_final.head()"""
    nb.cells.append(nbf.v4.new_code_cell(code_fe))
    
    # Final Visualization
    nb.cells.append(nbf.v4.new_markdown_cell("## 5. Final Correlation Heatmap\nChecking correlations post feature-engineering."))
    code_final_viz = """vis_final = Visualizer(df_final, OUTPUTS_DIR)
vis_final.plot_correlation_heatmap()"""
    nb.cells.append(nbf.v4.new_code_cell(code_final_viz))
    
    # Save Final
    nb.cells.append(nbf.v4.new_markdown_cell("## 6. Save Processed Data\nSaving the final dataset for modeling."))
    code_save = """import os
os.makedirs('../data/processed', exist_ok=True)
df_final.to_csv('../data/processed/cleaned_sales.csv', index=False)
print("Data preprocessing complete and saved to 'data/processed/cleaned_sales.csv'")"""
    nb.cells.append(nbf.v4.new_code_cell(code_save))
    
    # Write to file
    notebook_path = "d:/decodelab_intership/notebooks/EDA_and_Feature_Engineering.ipynb"
    os.makedirs(os.path.dirname(notebook_path), exist_ok=True)
    with open(notebook_path, 'w', encoding='utf-8') as f:
        nbf.write(nb, f)
    print(f"Notebook created at {notebook_path}")

if __name__ == "__main__":
    create_notebook()
