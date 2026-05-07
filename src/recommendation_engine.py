import pandas as pd

def generate_recommendation():

    # Load Dataset
    df = pd.read_csv("data/processed_shipping_data.csv")

    # Recommendation Logic
    df['recommendation_score'] = (
        df['warehouse_stock'] /
        (
            df['shipping_cost'] +
            df['delivery_days']
        )
    )

    # Best Recommendation
    recommendation = df.loc[
        df['recommendation_score'].idxmax()
    ]

    print("AI Recommendation Output")

    print(recommendation[
        [
            'factory_id',
            'shipping_cost',
            'delivery_days',
            'recommendation_score'
        ]
    ])

if __name__ == "__main__":
    generate_recommendation()
