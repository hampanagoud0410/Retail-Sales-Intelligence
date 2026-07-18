"""
Database Connection

Creates a connection to the SQLite database.
"""

import sqlite3
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATABASE_PATH = PROJECT_ROOT / "data" / "processed" / "retail_sales.db"


def get_connection():
    """
    Return SQLite database connection.
    """

    connection = sqlite3.connect(DATABASE_PATH)

    return connection