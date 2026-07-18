"""
Order Item Generator
"""

import random
from pathlib import Path

import pandas as pd

NUM_ORDERS = 50000
NUM_PRODUCTS = 55

order_items = []

order_item_id = 1

for order_id in range(1, NUM_ORDERS + 1):

    number_of_products = random.randint(1, 3)

    selected_products = random.sample(
        range(1, NUM_PRODUCTS + 1),
        number_of_products
    )

    for product_id in selected_products:

        order_items.append(
            {
                "order_item_id": order_item_id,
                "order_id": order_id,
                "product_id": product_id,
                "quantity": random.randint(1, 5),
                "discount": random.choice([0, 5, 10, 15, 20])
            }
        )

        order_item_id += 1

order_item_df = pd.DataFrame(order_items)

PROJECT_ROOT = Path(__file__).resolve().parents[2]

OUTPUT_PATH = PROJECT_ROOT / "data" / "raw" / "order_items.csv"

order_item_df.to_csv(
    OUTPUT_PATH,
    index=False
)

print("=" * 60)
print("Order Items generated successfully!")
print(f"Records : {len(order_item_df)}")
print(f"Saved to : {OUTPUT_PATH}")
print("=" * 60)