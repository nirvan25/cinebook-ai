import sqlite3


DB_NAME = "cinebook.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME, check_same_thread=False)
    initialize_database(conn)
    return conn


def initialize_database(conn):
    cursor = conn.cursor()

    # --------------------------------------------------
    # CREATE MOVIES TABLE
    # --------------------------------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            type TEXT,
            release_date INTEGER,
            price REAL
        )
    """)

    # --------------------------------------------------
    # CREATE BOOKINGS TABLE
    # --------------------------------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT,
            movie_name TEXT,
            tickets INTEGER,
            total_cost REAL
        )
    """)

    # --------------------------------------------------
    # SEED MOVIES IF EMPTY
    # --------------------------------------------------
    cursor.execute("SELECT COUNT(*) FROM movies")
    count = cursor.fetchone()[0]

    if count == 0:

        movies_data = [

            # CLASSIC
            ("Casablanca", "Drama", 1942, 200),
            ("Psycho", "Crime", 1960, 220),

            # GOLDEN
            ("The Godfather", "Crime", 1972, 250),
            ("Taxi Driver", "Crime", 1976, 230),
            ("Back to the Future", "Sci-Fi", 1985, 240),

            # MODERN
            ("The Shawshank Redemption", "Drama", 1994, 260),
            ("Fight Club", "Drama", 1999, 250),
            ("The Dark Knight", "Action", 2008, 300),

            # CONTEMPORARY
            ("Inception", "Sci-Fi", 2010, 250),
            ("Student of the Year", "Drama", 2012, 300),
            ("Interstellar", "Sci-Fi", 2014, 300),
            ("Avengers Endgame", "Action", 2019, 320),
            ("Joker", "Crime", 2019, 280),
            ("Parasite", "Thriller", 2019, 270)
        ]

        cursor.executemany(
            "INSERT INTO movies (name, type, release_date, price) VALUES (?, ?, ?, ?)",
            movies_data
        )

    conn.commit()