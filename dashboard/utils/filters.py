from .database import get_connection
import pandas as pd


def get_states():
    conn = get_connection()

    df = pd.read_sql(
        """
        SELECT DISTINCT state
        FROM stores
        ORDER BY state
        """,
        conn
    )

    conn.close()

    return ["All"] + df["state"].tolist()


def get_categories():
    conn = get_connection()

    df = pd.read_sql(
        """
        SELECT DISTINCT category_name
        FROM categories
        ORDER BY category_name
        """,
        conn
    )

    conn.close()

    return ["All"] + df["category_name"].tolist()


def get_years():
    conn = get_connection()

    df = pd.read_sql(
        """
        SELECT DISTINCT strftime('%Y', order_date) AS year
        FROM orders
        ORDER BY year
        """,
        conn
    )

    conn.close()

    return ["All"] + df["year"].tolist()