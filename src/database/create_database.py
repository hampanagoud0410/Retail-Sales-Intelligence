import sqlite3
from pathlib import Path

# Project root
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Database location
DATABASE_PATH = PROJECT_ROOT / "data" / "processed" / "retail_sales.db"

# SQL schema
SQL_FILE = PROJECT_ROOT / "sql" / "create_tables.sql"

# Create database
connection = sqlite3.connect(DATABASE_PATH)

with open(SQL_FILE, "r", encoding="utf-8") as file:
    connection.executescript(file.read())

connection.commit()
connection.close()

print("=" * 50)
print("Database created successfully!")
print(DATABASE_PATH)
print("=" * 50)