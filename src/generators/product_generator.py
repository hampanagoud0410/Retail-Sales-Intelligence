"""
Product Data Generator
"""

from pathlib import Path
import random

import pandas as pd

from src.generators.common import PRODUCT_CATALOG

products = []

product_id = 1

for category_id, (category, items) in enumerate(PRODUCT_CATALOG.items(), start=1):

    for brand, product_name in items:

        cost_price = random.randint(500, 5000)
        selling_price = cost_price + random.randint(100, 2000)

        products.append(
            {
                "product_id": product_id,
                "category_id": category_id,
                "product_name": product_name,
                "brand": brand,
                "cost_price": cost_price,
                "selling_price": selling_price,
            }
        )

        product_id += 1

product_df = pd.DataFrame(products)

PROJECT_ROOT = Path(__file__).resolve().parents[2]

OUTPUT_PATH = PROJECT_ROOT / "data" / "raw" / "products.csv"

product_df.to_csv(OUTPUT_PATH, index=False)

print("=" * 60)
print("Products generated successfully!")
print(f"Records : {len(product_df)}")
print(f"Saved to : {OUTPUT_PATH}")
print("=" * 60)