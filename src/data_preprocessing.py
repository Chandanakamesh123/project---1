import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def preprocess_data():

    # Load Dataset
    df = pd.read_csv("data/raw_shipping_data.csv")

    # Remove Duplicates
    df.drop_duplicates(inplace=True)

    # Handle Missing Values
    df.fillna(method='ffill', inplace=True)

    # Encode Categorical Features
    le = LabelEncoder()

    categorical_cols = [
        'customer_region',
        'season',
        'transport_mode',
        'factory_id',
        'product_id'
    ]

    for col in categorical_cols:
        df[col] = le.fit_transform(df[col])

    # Scale Numerical Features
    scaler = StandardScaler()

    numerical_cols = [
        'warehouse_stock',
        'shipping_cost',
        'delivery_days',
        'route_distance',
        'factory_capacity',
        'order_quantity'
    ]

    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

    # Save Processed Data
    df.to_csv("data/processed_shipping_data.csv", index=False)

    print("Data preprocessing completed successfully.")

if __name__ == "__main__":
    preprocess_data()
