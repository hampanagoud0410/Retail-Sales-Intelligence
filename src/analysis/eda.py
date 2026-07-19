import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# -------------------------------
# Database Connection
# -------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]

DB_PATH = PROJECT_ROOT / "data" / "processed" / "retail_sales.db"
REPORT_PATH = PROJECT_ROOT / "reports"

REPORT_PATH.mkdir(exist_ok=True)

conn = sqlite3.connect(DB_PATH)

# -------------------------------
# Revenue by Category
# -------------------------------


def category_sales():
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

    plt.figure(figsize=(10,6))
    plt.bar(df["category_name"], df["revenue"])

    plt.xticks(rotation=45)
    plt.title("Revenue by Category")
    plt.xlabel("Category")
    plt.ylabel("Revenue")

    plt.tight_layout()
    plt.savefig(REPORT_PATH / "category_sales.png")
    plt.close()

    print("✔ category_sales.png created")

def state_sales():
    query = """
    SELECT
        s.state,
        ROUND(SUM((p.selling_price - oi.discount) * oi.quantity),2) AS revenue
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

    plt.figure(figsize=(10,6))
    plt.bar(df["state"], df["revenue"])

    plt.xticks(rotation=45)
    plt.title("Revenue by State")
    plt.xlabel("State")
    plt.ylabel("Revenue")

    plt.tight_layout()
    plt.savefig(REPORT_PATH / "state_sales.png")
    plt.close()

    print("✔ state_sales.png created")

def monthly_sales():
    query = """
    SELECT
        strftime('%Y-%m', o.order_date) AS month,
        ROUND(SUM((p.selling_price - oi.discount) * oi.quantity),2) AS revenue
    FROM orders o
    JOIN order_items oi
        ON o.order_id = oi.order_id
    JOIN products p
        ON oi.product_id = p.product_id
    GROUP BY month
    ORDER BY month;
    """

    df = pd.read_sql(query, conn)

    plt.figure(figsize=(12,6))
    plt.plot(df["month"], df["revenue"], marker="o")

    plt.xticks(rotation=45)
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue")

    plt.tight_layout()
    plt.savefig(REPORT_PATH / "monthly_sales.png")
    plt.close()

    print("✔ monthly_sales.png created")

def top_products():
    query = """
    SELECT
        p.product_name,
        ROUND(SUM((p.selling_price-oi.discount)*oi.quantity),2) AS revenue
    FROM products p
    JOIN order_items oi
        ON p.product_id = oi.product_id
    GROUP BY p.product_name
    ORDER BY revenue DESC
    LIMIT 10;
    """

    df = pd.read_sql(query, conn)

    plt.figure(figsize=(10,6))
    plt.barh(df["product_name"], df["revenue"])

    plt.title("Top 10 Products by Revenue")
    plt.xlabel("Revenue")
    plt.ylabel("Product")

    plt.tight_layout()
    plt.savefig(REPORT_PATH / "top_products.png")
    plt.close()

    print("✔ top_products.png created")

def payment_methods():
    query = """
    SELECT
        payment_method,
        COUNT(*) AS total
    FROM payments
    GROUP BY payment_method;
    """

    df = pd.read_sql(query, conn)

    plt.figure(figsize=(7,7))
    plt.pie(
        df["total"],
        labels=df["payment_method"],
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Payment Method Distribution")

    plt.tight_layout()
    plt.savefig(REPORT_PATH / "payment_methods.png")
    plt.close()

    print("✔ payment_methods.png created")

def return_analysis():
    query = """
    SELECT
        return_reason,
        COUNT(*) AS total
    FROM returns
    GROUP BY return_reason;
    """

    df = pd.read_sql(query, conn)

    plt.figure(figsize=(8,8))
    plt.pie(
        df["total"],
        labels=df["return_reason"],
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Return Reasons")

    plt.tight_layout()
    plt.savefig(REPORT_PATH / "return_analysis.png")
    plt.close()

    print("✔ return_analysis.png created")

def customer_age_distribution():
    query = """
    SELECT age
    FROM customers;
    """

    df = pd.read_sql(query, conn)

    plt.figure(figsize=(10,6))
    plt.hist(df["age"], bins=10)

    plt.title("Customer Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Customers")

    plt.tight_layout()
    plt.savefig(REPORT_PATH / "customer_age_distribution.png")
    plt.close()

    print("✔ customer_age_distribution.png created")


def gender_distribution():
    query = """
    SELECT
        gender,
        COUNT(*) AS total
    FROM customers
    GROUP BY gender;
    """

    df = pd.read_sql(query, conn)

    plt.figure(figsize=(6,6))
    plt.pie(
        df["total"],
        labels=df["gender"],
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Gender Distribution")

    plt.tight_layout()
    plt.savefig(REPORT_PATH / "gender_distribution.png")
    plt.close()

    print("✔ gender_distribution.png created")


def store_sales():
    query = """
    SELECT
        s.store_name,
        ROUND(SUM((p.selling_price-oi.discount)*oi.quantity),2) AS revenue
    FROM stores s
    JOIN orders o
        ON s.store_id = o.store_id
    JOIN order_items oi
        ON o.order_id = oi.order_id
    JOIN products p
        ON oi.product_id = p.product_id
    GROUP BY s.store_name
    ORDER BY revenue DESC;
    """

    df = pd.read_sql(query, conn)

    plt.figure(figsize=(10,6))
    plt.bar(df["store_name"], df["revenue"])

    plt.xticks(rotation=45)
    plt.title("Store-wise Revenue")
    plt.xlabel("Store")
    plt.ylabel("Revenue")

    plt.tight_layout()
    plt.savefig(REPORT_PATH / "store_sales.png")
    plt.close()

    print("✔ store_sales.png created")





def main():
    category_sales()
    state_sales()
    monthly_sales()
    top_products()
    payment_methods()
    return_analysis()
    customer_age_distribution()
    gender_distribution()
    store_sales()

    conn.close()
if __name__ == "__main__":
    main()