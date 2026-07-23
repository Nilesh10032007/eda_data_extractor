import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DataPreprocessor:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def handle_missing_values(self):
        """
        Handles missing values based on percentages:
        <5% -> Drop rows
        5-20% -> Median Imputation
        >20% -> KNN Imputation
        """
        missing_percentages = self.df.isnull().sum() / len(self.df) * 100
        
        for col, missing_pct in missing_percentages.items():
            if missing_pct == 0:
                continue
                
            logging.info(f"Column '{col}' has {missing_pct:.2f}% missing values.")
            
            if missing_pct < 5:
                logging.info(f"Dropping rows for '{col}' (<5% missing).")
                self.df.dropna(subset=[col], inplace=True)
            elif 5 <= missing_pct <= 20:
                logging.info(f"Applying Median imputation for '{col}' (5-20% missing).")
                self.df[col] = self.df[col].fillna(self.df[col].median())
            else:
                logging.info(f"Applying KNN imputation for '{col}' (>20% missing).")
                # KNN imputer requires numerical data. If categorical, fallback to mode.
                if pd.api.types.is_numeric_dtype(self.df[col]):
                    imputer = KNNImputer(n_neighbors=5)
                    self.df[col] = imputer.fit_transform(self.df[[col]])
                else:
                    logging.info(f"Column '{col}' is categorical. Falling back to Mode imputation.")
                    self.df[col] = self.df[col].fillna(self.df[col].mode()[0])
        
        return self.df

    def detect_and_handle_outliers(self, method='iqr', action='winsorize'):
        """
        Detects and handles outliers.
        method: 'iqr' or 'zscore'
        action: 'winsorize' or 'remove'
        """
        numerical_cols = self.df.select_dtypes(include=[np.number]).columns
        
        for col in numerical_cols:
            if method == 'iqr':
                Q1 = self.df[col].quantile(0.25)
                Q3 = self.df[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR
            elif method == 'zscore':
                mean = self.df[col].mean()
                std = self.df[col].std()
                lower_bound = mean - 3 * std
                upper_bound = mean + 3 * std
            else:
                raise ValueError("Method must be 'iqr' or 'zscore'")
                
            outliers_count = ((self.df[col] < lower_bound) | (self.df[col] > upper_bound)).sum()
            
            if outliers_count > 0:
                logging.info(f"Detected {outliers_count} outliers in '{col}' using {method.upper()} method.")
                if action == 'winsorize':
                    # Cap the values at the bounds
                    self.df[col] = np.where(self.df[col] < lower_bound, lower_bound, self.df[col])
                    self.df[col] = np.where(self.df[col] > upper_bound, upper_bound, self.df[col])
                    logging.info(f"Winsorized outliers in '{col}'.")
                elif action == 'remove':
                    self.df = self.df[(self.df[col] >= lower_bound) & (self.df[col] <= upper_bound)]
                    logging.info(f"Removed outliers in '{col}'.")
                    
        return self.df
