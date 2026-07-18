"""
Create SQLite Database
"""

from pathlib import Path
import sqlite3


PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATABASE_PATH = PROJECT_ROOT / "data" / "processed" / "retail_sales.db"

SQL_FILE = PROJECT_ROOT / "sql" / "create_tables.sql"


def create_database():

    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()

    with open(SQL_FILE, "r", encoding="utf-8") as file:
        cursor.executescript(file.read())

    connection.commit()

    connection.close()

    print("=" * 60)
    print("Database created successfully!")
    print(DATABASE_PATH)
    print("=" * 60)


if __name__ == "__main__":
    create_database()