import pandas as pd

def create_features():

    # Load Processed Dataset
    df = pd.read_csv("data/processed_shipping_data.csv")

    # Create Cost Per Distance Feature
    df['cost_per_distance'] = (
        df['shipping_cost'] / (df['route_distance'] + 1)
    )

    # Create Delivery Efficiency Feature
    df['delivery_efficiency'] = (
        df['order_quantity'] / (df['delivery_days'] + 1)
    )

    # Create Inventory Ratio Feature
    df['inventory_ratio'] = (
        df['warehouse_stock'] / (df['factory_capacity'] + 1)
    )

    # Save Updated Dataset
    df.to_csv("data/processed_shipping_data.csv", index=False)

    print("Feature engineering completed successfully.")

if __name__ == "__main__":
    create_features()
