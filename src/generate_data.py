import pandas as pd
import numpy as np
import os

def generate_ecommerce_data(num_rows=2000):
    np.random.seed(42)
    
    data = {
        'OrderID': [f"ORD{i:06d}" for i in range(1, num_rows + 1)],
        'Date': pd.date_range(start='2023-01-01', periods=num_rows, freq='h'),
        'CustomerID': [f"C{np.random.randint(10000, 99999)}" for _ in range(num_rows)],
        'Product': np.random.choice(['Laptop', 'Monitor', 'Phone', 'Desk', 'Chair', 'Tablet', 'Printer'], num_rows),
        'Quantity': np.random.randint(1, 6, num_rows),
        'UnitPrice': np.random.uniform(50, 1500, num_rows),
        'ShippingAddress': [f"{np.random.randint(100, 999)} Main St" for _ in range(num_rows)],
        'PaymentMethod': np.random.choice(['Credit Card', 'Debit Card', 'Online', 'Cash', 'Gift Card'], num_rows),
        'OrderStatus': np.random.choice(['Shipped', 'Delivered', 'Cancelled', 'Pending', 'Returned'], num_rows, p=[0.5, 0.2, 0.1, 0.1, 0.1]),
        'ItemsInCart': np.random.randint(1, 10, num_rows),
        'ReferralSource': np.random.choice(['Instagram', 'Facebook', 'Google', 'Email', 'Referral'], num_rows),
    }
    
    df = pd.DataFrame(data)
    
    # Introduce Outliers in 'UnitPrice'
    outlier_indices = np.random.choice(num_rows, size=int(num_rows * 0.03), replace=False)
    df.loc[outlier_indices, 'UnitPrice'] *= np.random.uniform(5, 10, len(outlier_indices))
    
    # Missing value scenarios
    # 1. <5% Missing -> 'Quantity' (Approx 3%)
    q_missing = np.random.choice(num_rows, size=int(num_rows * 0.03), replace=False)
    df.loc[q_missing, 'Quantity'] = np.nan
    
    # 2. 5-20% Missing -> 'ItemsInCart' (Approx 15%)
    cart_missing = np.random.choice(num_rows, size=int(num_rows * 0.15), replace=False)
    df.loc[cart_missing, 'ItemsInCart'] = np.nan
    
    # 3. >20% Missing -> 'UnitPrice' (Wait, UnitPrice is too important. Let's create a 'CustomerRating' column)
    df['CustomerRating'] = np.random.uniform(1.0, 5.0, num_rows)
    rating_missing = np.random.choice(num_rows, size=int(num_rows * 0.25), replace=False)
    df.loc[rating_missing, 'CustomerRating'] = np.nan
    
    # Base TotalPrice
    df['TotalPrice'] = df['Quantity'].fillna(1) * df['UnitPrice'].fillna(df['UnitPrice'].mean())
    
    os.makedirs('d:/decodelab_intership/data/raw', exist_ok=True)
    df.to_csv('d:/decodelab_intership/data/raw/ecommerce_sales.csv', index=False)
    print(f"Dataset with {num_rows} rows generated successfully!")

if __name__ == '__main__':
    generate_ecommerce_data()
