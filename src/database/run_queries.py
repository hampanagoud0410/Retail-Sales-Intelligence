"""
Run SQL Queries
"""

from pathlib import Path

import pandas as pd
from tabulate import tabulate

from src.database.db_connection import get_connection

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SQL_FOLDER = PROJECT_ROOT / "sql"


def run_query(filename):

    conn = get_connection()

    sql_path = SQL_FOLDER / filename

    with open(sql_path, "r", encoding="utf-8") as file:
        query = file.read()

    df = pd.read_sql_query(query, conn)

    print("\n" + "=" * 70)
    print(filename)
    print("=" * 70)

    print(tabulate(df, headers="keys", tablefmt="grid", showindex=False))

    conn.close()


def main():

    queries = [
    "01_total_sales.sql",
    "02_total_profit.sql",
    "03_top_products.sql",
    "04_sales_by_state.sql",
    "05_monthly_sales.sql",
    "06_payment_analysis.sql",
    "07_return_analysis.sql",
    "08_category_sales.sql",
    ]

    for query in queries:
        run_query(query)


if __name__ == "__main__":
    main()