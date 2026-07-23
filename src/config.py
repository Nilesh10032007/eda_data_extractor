import os

# Base paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
RAW_DATA_PATH = os.path.join(DATA_DIR, 'raw', 'ecommerce_sales.csv')
PROCESSED_DATA_PATH = os.path.join(DATA_DIR, 'processed', 'cleaned_sales.csv')
OUTPUTS_DIR = os.path.join(BASE_DIR, 'outputs')

# Create directories if they don't exist
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(os.path.join(DATA_DIR, 'raw'), exist_ok=True)
os.makedirs(os.path.join(DATA_DIR, 'processed'), exist_ok=True)
os.makedirs(OUTPUTS_DIR, exist_ok=True)

# Preprocessing parameters
MISSING_VALUE_THRESHOLDS = {
    'drop': 0.05,
    'impute_simple': 0.20
    # > 20% handled by KNN
}

# Outlier parameters
OUTLIER_METHOD = 'iqr' # or 'zscore'
Z_SCORE_THRESHOLD = 3.0
