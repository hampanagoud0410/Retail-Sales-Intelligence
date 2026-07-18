"""
Order Data Generator

Generates random retail orders.
"""

import random
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd

# -----------------------------
# Configuration
# -----------------------------

NUM_ORDERS = 50000
NUM_CUSTOMERS = 10000
NUM_STORES = 10

# -----------------------------
# Generate Orders
# -----------------------------

orders = []

start_date = datetime(2022, 1, 1)
end_date = datetime(2025, 12, 31)

days_between = (end_date - start_date).days

for order_id in range(1, NUM_ORDERS + 1):

    customer_id = random.randint(1, NUM_CUSTOMERS)

    store_id = random.randint(1, NUM_STORES)

    order_date = start_date + timedelta(days=random.randint(0, days_between))

    orders.append(
        {
            "order_id": order_id,
            "customer_id": customer_id,
            "store_id": store_id,
            "order_date": order_date.strftime("%Y-%m-%d"),
        }
    )

# -----------------------------
# Save CSV
# -----------------------------

order_df = pd.DataFrame(orders)

PROJECT_ROOT = Path(__file__).resolve().parents[2]

OUTPUT_PATH = PROJECT_ROOT / "data" / "raw" / "orders.csv"

order_df.to_csv(OUTPUT_PATH, index=False)

print("=" * 60)
print("Orders generated successfully!")
print(f"Records : {len(order_df)}")
print(f"Saved to : {OUTPUT_PATH}")
print("=" * 60)