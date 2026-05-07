import pandas as pd

def allocate_factory():

    # Load Dataset
    df = pd.read_csv("data/processed_shipping_data.csv")

    # Factory Scoring Formula
    df['factory_score'] = (
        df['warehouse_stock'] /
        (
            df['shipping_cost'] +
            df['delivery_days'] +
            df['factory_capacity']
        )
    )

    # Recommend Best Factory
    best_factory = df.loc[
        df['factory_score'].idxmax()
    ]

    print("Recommended Factory Allocation")

    print(best_factory[['factory_id', 'factory_score']])

if __name__ == "__main__":
    allocate_factory()
