import pandas as pd
import os
import sys

# Add src to path
sys.path.append(os.path.abspath('src'))

from src.preprocessing import DataPreprocessor
from src.feature_engineering import FeatureEngineer
from src.visualization import Visualizer
from src.config import RAW_DATA_PATH, PROCESSED_DATA_PATH, OUTPUTS_DIR
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info("Starting Advanced EDA & Feature Engineering Pipeline")
    
    # 1. Load Data
    logging.info(f"Loading data from {RAW_DATA_PATH}")
    df = pd.read_csv(RAW_DATA_PATH)
    
    # 2. Initial EDA Visualizations
    logging.info("Generating initial visualizations...")
    vis = Visualizer(df, OUTPUTS_DIR)
    vis.plot_missing_values()
    vis.plot_histograms()
    vis.plot_boxplots()
    
    # 3. Preprocessing
    logging.info("Running Preprocessing...")
    preprocessor = DataPreprocessor(df)
    df_clean = preprocessor.handle_missing_values()
    df_clean = preprocessor.detect_and_handle_outliers(method='iqr', action='winsorize')
    
    # 4. Feature Engineering
    logging.info("Running Feature Engineering...")
    engineer = FeatureEngineer(df_clean)
    df_featured = engineer.engineer_features()
    df_featured = engineer.encode_categorical_features()
    df_final = engineer.check_multicollinearity(threshold=0.85)
    
    # 5. Final Visualizations
    logging.info("Generating final visualizations...")
    vis_final = Visualizer(df_final, OUTPUTS_DIR)
    vis_final.plot_correlation_heatmap()
    
    # 6. Save final dataset
    logging.info(f"Saving processed data to {PROCESSED_DATA_PATH}")
    os.makedirs(os.path.dirname(PROCESSED_DATA_PATH), exist_ok=True)
    df_final.to_csv(PROCESSED_DATA_PATH, index=False)
    
    logging.info("Pipeline completed successfully!")

if __name__ == "__main__":
    main()
