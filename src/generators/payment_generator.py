"""
Payment Data Generator
"""

import random
from pathlib import Path

import pandas as pd

from src.generators.common import PAYMENT_METHODS, PAYMENT_STATUS

NUM_ORDERS = 50000

payments = []

for payment_id in range(1, NUM_ORDERS + 1):

    payments.append(
        {
            "payment_id": payment_id,
            "order_id": payment_id,
            "payment_method": random.choice(PAYMENT_METHODS),
            "payment_status": random.choices(
                PAYMENT_STATUS,
                weights=[95, 5, 0],
                k=1
            )[0],
        }
    )

payment_df = pd.DataFrame(payments)

PROJECT_ROOT = Path(__file__).resolve().parents[2]

OUTPUT_PATH = PROJECT_ROOT / "data" / "raw" / "payments.csv"

payment_df.to_csv(
    OUTPUT_PATH,
    index=False
)

print("=" * 60)
print("Payments generated successfully!")
print(f"Records : {len(payment_df)}")
print(f"Saved to : {OUTPUT_PATH}")
print("=" * 60)