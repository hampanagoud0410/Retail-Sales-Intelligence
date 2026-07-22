from .database import get_connection
import pandas as pd


def load_dashboard_data():
    conn = get_connection()

    query = """
    SELECT
        o.order_id,
        o.customer_id,
        o.order_date,

        s.store_name,
        s.state,

        p.product_id,
        p.product_name,
        c.category_name,

        oi.quantity,
        oi.discount,

        p.cost_price,
        p.selling_price,

        pay.payment_method,

        r.return_reason

    FROM orders o

    JOIN stores s
        ON o.store_id = s.store_id

    JOIN order_items oi
        ON o.order_id = oi.order_id

    JOIN products p
        ON oi.product_id = p.product_id

    JOIN categories c
        ON p.category_id = c.category_id

    LEFT JOIN payments pay
        ON o.order_id = pay.order_id

    LEFT JOIN returns r
        ON oi.order_item_id = r.order_item_id
    """

    df = pd.read_sql(query, conn)
    conn.close()

    df["Revenue"] = (
        (df["selling_price"] - df["discount"])
        * df["quantity"]
    )

    df["Profit"] = (
        (
            df["selling_price"]
            - df["cost_price"]
            - df["discount"]
        )
        * df["quantity"]
    )

    df["Year"] = pd.to_datetime(
        df["order_date"]
    ).dt.year.astype(str)

    return df