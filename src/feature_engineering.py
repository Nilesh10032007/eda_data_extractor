import pandas as pd
import numpy as np
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FeatureEngineer:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def engineer_features(self):
        """
        Creates meaningful engineered features.
        """
        logging.info("Engineering new features...")
        
        # 1. Datetime feature: 'OrderDayOfWeek' and 'OrderHour'
        if 'Date' in self.df.columns:
            self.df['Date'] = pd.to_datetime(self.df['Date'])
            self.df['OrderDayOfWeek'] = self.df['Date'].dt.dayofweek
            self.df['OrderHour'] = self.df['Date'].dt.hour
            self.df['IsWeekend'] = self.df['OrderDayOfWeek'].apply(lambda x: 1 if x >= 5 else 0)
            logging.info("Created 'OrderDayOfWeek', 'OrderHour', and 'IsWeekend' features.")

        # 2. TotalCartValue (if TotalPrice and ItemsInCart exist)
        if 'TotalPrice' in self.df.columns and 'ItemsInCart' in self.df.columns:
            # Prevent division by zero
            self.df['AvgItemValueInCart'] = self.df['TotalPrice'] / (self.df['ItemsInCart'] + 1e-5)
            logging.info("Created 'AvgItemValueInCart' feature.")
            
        # 3. Customer Frequency (Count of orders per customer)
        if 'CustomerID' in self.df.columns:
            customer_counts = self.df['CustomerID'].value_counts().to_dict()
            self.df['CustomerOrderCount'] = self.df['CustomerID'].map(customer_counts)
            logging.info("Created 'CustomerOrderCount' feature.")
            
        return self.df

    def encode_categorical_features(self):
        """
        Encodes categorical features using One-Hot Encoding.
        """
        categorical_cols = self.df.select_dtypes(include=['object', 'category']).columns
        # Excluding ID and Date columns from encoding
        exclude_cols = ['OrderID', 'Date', 'CustomerID', 'ShippingAddress']
        cols_to_encode = [col for col in categorical_cols if col not in exclude_cols]
        
        if cols_to_encode:
            logging.info(f"One-Hot Encoding features: {cols_to_encode}")
            self.df = pd.get_dummies(self.df, columns=cols_to_encode, drop_first=True)
            
        return self.df

    def check_multicollinearity(self, threshold=0.85):
        """
        Checks for multicollinearity and removes highly correlated features.
        """
        numerical_cols = self.df.select_dtypes(include=[np.number]).columns
        corr_matrix = self.df[numerical_cols].corr().abs()
        
        # Select upper triangle of correlation matrix
        upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
        
        # Find features with correlation greater than threshold
        to_drop = [column for column in upper.columns if any(upper[column] > threshold)]
        
        if to_drop:
            logging.info(f"Removing highly correlated features (> {threshold}): {to_drop}")
            self.df.drop(columns=to_drop, inplace=True)
        else:
            logging.info("No highly correlated features found.")
            
        return self.df
