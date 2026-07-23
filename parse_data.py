import re
import pandas as pd

def parse_transcript_and_create_csv():
    transcript_path = r"C:\Users\Lenovo\.gemini\antigravity\brain\0b9db6ce-142a-45e2-9d21-492d040d20c1\.system_generated\logs\transcript_full.jsonl"
    
    with open(transcript_path, 'r', encoding='utf-8') as f:
        content = f.read()
                
    # Parse lines
    pattern = re.compile(
        r"(ORD\d+)(\d{4}-\d{2}-\d{2})(C\d+)\s+"                 # OrderID, Date, CustomerID
        r"([A-Za-z]+)\s+"                                       # Product
        r"(\d+)\s+"                                             # Quantity
        r"([\d.]+)\s+"                                          # UnitPrice
        r"(\d+\s+Main\s+St)"                                    # ShippingAddress
        r"(Debit\s+Card|Credit\s+Card|Online|Cash|Gift\s+Card)\s*"  # PaymentMethod
        r"(Shipped|Cancelled|Pending|Returned|Delivered)\s+"    # OrderStatus
        r"(TRK\d+)\s+"                                          # TrackingNumber
        r"(\d+)\s+"                                             # ItemsInCart
        r"([A-Z0-9!]+)?\s*"                                     # CouponCode (Optional)
        r"(Instagram|Referral|Email|Facebook|Google)\s+"        # ReferralSource
        r"([\d.]+)"                                             # TotalPrice
    )
    
    parsed_data = []
    for match in pattern.finditer(content):
        parsed_data.append(match.groups())
            
    # Remove duplicates
    parsed_data = list(set(parsed_data))
    
    df = pd.DataFrame(parsed_data, columns=[
        "OrderID", "Date", "CustomerID", "Product", "Quantity", 
        "UnitPrice", "ShippingAddress", "PaymentMethod", "OrderStatus", 
        "TrackingNumber", "ItemsInCart", "CouponCode", "ReferralSource", "TotalPrice"
    ])
    
    # Fill empty coupons with None
    df['CouponCode'] = df['CouponCode'].fillna("NONE")
    
    out_path = "d:/decodelab_intership/data/raw/ecommerce_sales.csv"
    df.to_csv(out_path, index=False)
    print(f"Successfully saved {len(df)} rows to {out_path}")

if __name__ == "__main__":
    parse_transcript_and_create_csv()
    
    parsed_data = []
    for line in ocr_lines:
        match = pattern.search(line)
        if match:
            parsed_data.append(match.groups())
        else:
            print("Failed to parse:", line)
            
    df = pd.DataFrame(parsed_data, columns=[
        "OrderID", "Date", "CustomerID", "Product", "Quantity", 
        "UnitPrice", "ShippingAddress", "PaymentMethod", "OrderStatus", 
        "TrackingNumber", "ItemsInCart", "CouponCode", "ReferralSource", "TotalPrice"
    ])
    
    # Fill empty coupons with None
    df['CouponCode'] = df['CouponCode'].fillna("NONE")
    
    out_path = "d:/decodelab_intership/data/raw/ecommerce_sales.csv"
    df.to_csv(out_path, index=False)
    print(f"Successfully saved {len(df)} rows to {out_path}")

if __name__ == "__main__":
    parse_transcript_and_create_csv()

