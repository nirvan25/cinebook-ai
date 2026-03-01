import sqlite3

DATABASE_PATH = "database/cinebook.db"


def initialize_db():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    # Movies table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            type TEXT,
            release_date TEXT,
            price REAL NOT NULL
        )
    """)

    # Bookings table
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