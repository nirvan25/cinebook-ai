import sqlite3
import os

DB_PATH = os.path.join("database", "cinebook.db")

def connect():
    return sqlite3.connect(DB_PATH)

def initialize_db():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        type TEXT,
        release_date TEXT,
        price REAL NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bookings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT NOT NULL,
        mobile TEXT,
        movie_name TEXT,
        tickets INTEGER,
        seat_type TEXT,
        total_cost REAL,
        show_time TEXT
    )
    """)

    conn.commit()
    conn.close()