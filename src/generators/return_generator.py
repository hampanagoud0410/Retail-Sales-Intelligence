"""
Return Data Generator
"""

import random
from pathlib import Path

import pandas as pd

from src.generators.common import RETURN_REASONS

PROJECT_ROOT = Path(__file__).resolve().parents[2]

ORDER_ITEMS_PATH = PROJECT_ROOT / "data" / "raw" / "order_items.csv"

order_items = pd.read_csv(ORDER_ITEMS_PATH)

# Select approximately 5% of order items for returns
returns = order_items.sample(frac=0.05, random_state=42)

return_records = []

for return_id, (_, row) in enumerate(returns.iterrows(), start=1):

    return_records.append(
        {
            "return_id": return_id,
            "order_item_id": row["order_item_id"],
            "return_reason": random.choice(RETURN_REASONS),
            "return_date": "2025-01-01"
        }
    )

return_df = pd.DataFrame(return_records)

OUTPUT_PATH = PROJECT_ROOT / "data" / "raw" / "returns.csv"

return_df.to_csv(
    OUTPUT_PATH,
    index=False
)

print("=" * 60)
print("Returns generated successfully!")
print(f"Records : {len(return_df)}")
print(f"Saved to : {OUTPUT_PATH}")
print("=" * 60)
