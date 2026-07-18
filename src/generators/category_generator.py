"""
Category Data Generator

Generates product categories for the
Retail Sales Intelligence project.
"""

from pathlib import Path

import pandas as pd

from src.generators.common import CATEGORIES

# Create category records
categories = []

for category_id, category_name in enumerate(CATEGORIES, start=1):
    categories.append(
        {
            "category_id": category_id,
            "category_name": category_name,
        }
    )

# Convert to DataFrame
category_df = pd.DataFrame(categories)

# Project root
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Output file
OUTPUT_PATH = PROJECT_ROOT / "data" / "raw" / "categories.csv"

# Save CSV
category_df.to_csv(OUTPUT_PATH, index=False)

print("=" * 60)
print("Category dataset generated successfully!")
print(f"Records : {len(category_df)}")
print(f"Saved to: {OUTPUT_PATH}")
print("=" * 60)