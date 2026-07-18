"""
Store Data Generator
"""

from pathlib import Path

import pandas as pd

from src.generators.common import STORES

stores = []

for store_id, (store_name, city, state) in enumerate(STORES, start=1):

    stores.append(
        {
            "store_id": store_id,
            "store_name": store_name,
            "city": city,
            "state": state,
        }
    )

store_df = pd.DataFrame(stores)

PROJECT_ROOT = Path(__file__).resolve().parents[2]

OUTPUT_PATH = PROJECT_ROOT / "data" / "raw" / "stores.csv"

store_df.to_csv(OUTPUT_PATH, index=False)

print("=" * 60)
print("Store dataset generated successfully!")
print(f"Records : {len(store_df)}")
print(f"Saved to : {OUTPUT_PATH}")
print("=" * 60)
