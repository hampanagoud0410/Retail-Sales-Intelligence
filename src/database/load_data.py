"""
Load CSV files into SQLite database.
"""

from pathlib import Path

import pandas as pd

from src.database.db_connection import get_connection

PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DATA = PROJECT_ROOT / "data" / "raw"


def load_table(connection, filename, table_name):
    """Load a CSV file into a database table."""

    csv_path = RAW_DATA / filename

    df = pd.read_csv(csv_path)

    df.to_sql(
        table_name,
        connection,
        if_exists="append",
        index=False
    )

    print(f"Loaded {filename} → {table_name} ({len(df)} rows)")


def main():

    connection = get_connection()

    load_table(connection, "customers.csv", "customers")
    load_table(connection, "categories.csv", "categories")
    load_table(connection, "products.csv", "products")
    load_table(connection, "stores.csv", "stores")
    load_table(connection, "orders.csv", "orders")
    load_table(connection, "order_items.csv", "order_items")
    load_table(connection, "payments.csv", "payments")
    load_table(connection, "returns.csv", "returns")

    connection.commit()
    connection.close()

    print("\nAll data loaded successfully!")


if __name__ == "__main__":
    main()