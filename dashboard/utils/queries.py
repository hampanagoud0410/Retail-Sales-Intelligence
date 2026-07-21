from .database import get_connection
import pandas as pd


def total_revenue():
    conn = get_connection()

    query = """
    SELECT
        ROUND(SUM((p.selling_price-oi.discount)*oi.quantity),2) revenue
    FROM products p
    JOIN order_items oi
        ON p.product_id=oi.product_id;
    """

    value = pd.read_sql(query, conn).iloc[0, 0]
    conn.close()

    return value


def total_orders():
    conn = get_connection()

    value = pd.read_sql(
        "SELECT COUNT(*) total FROM orders;",
        conn
    ).iloc[0, 0]

    conn.close()

    return value


def total_customers():
    conn = get_connection()

    value = pd.read_sql(
        "SELECT COUNT(*) total FROM customers;",
        conn
    ).iloc[0, 0]

    conn.close()

    return value


def total_profit():
    conn = get_connection()

    query = """
    SELECT
        ROUND(SUM((p.selling_price-p.cost_price-oi.discount)*oi.quantity),2)
    FROM products p
    JOIN order_items oi
        ON p.product_id=oi.product_id;
    """

    value = pd.read_sql(query, conn).iloc[0, 0]

    conn.close()

    return value
def monthly_sales():
    conn = get_connection()

    query = """
    SELECT
        strftime('%Y-%m', o.order_date) AS month,
        ROUND(SUM((p.selling_price-oi.discount)*oi.quantity),2) revenue
    FROM orders o
    JOIN order_items oi
        ON o.order_id = oi.order_id
    JOIN products p
        ON oi.product_id = p.product_id
    GROUP BY month
    ORDER BY month;
    """

    df = pd.read_sql(query, conn)
    conn.close()

    return df


def category_sales():
    conn = get_connection()

    query = """
    SELECT
        c.category_name,
        ROUND(SUM((p.selling_price-oi.discount)*oi.quantity),2) revenue
    FROM categories c
    JOIN products p
        ON c.category_id=p.category_id
    JOIN order_items oi
        ON p.product_id=oi.product_id
    GROUP BY c.category_name
    ORDER BY revenue DESC;
    """

    df = pd.read_sql(query, conn)
    conn.close()

    return df
def state_sales():
    conn = get_connection()

    query = """
    SELECT
        s.state,
        ROUND(SUM((p.selling_price-oi.discount)*oi.quantity),2) revenue
    FROM stores s
    JOIN orders o
        ON s.store_id = o.store_id
    JOIN order_items oi
        ON o.order_id = oi.order_id
    JOIN products p
        ON oi.product_id = p.product_id
    GROUP BY s.state
    ORDER BY revenue DESC;
    """

    df = pd.read_sql(query, conn)
    conn.close()

    return df


def top_products():
    conn = get_connection()

    query = """
    SELECT
        p.product_name,
        ROUND(SUM((p.selling_price-oi.discount)*oi.quantity),2) revenue
    FROM products p
    JOIN order_items oi
        ON p.product_id = oi.product_id
    GROUP BY p.product_name
    ORDER BY revenue DESC
    LIMIT 10;
    """

    df = pd.read_sql(query, conn)
    conn.close()

    return df
def payment_methods():
    conn = get_connection()

    query = """
    SELECT
        payment_method,
        COUNT(*) total
    FROM payments
    GROUP BY payment_method;
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df


def return_analysis():
    conn = get_connection()

    query = """
    SELECT
        return_reason,
        COUNT(*) total
    FROM returns
    GROUP BY return_reason;
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df