import sqlite3

DATABASE_PATH = "database/cinebook.db"


def add_movie(name, genre, release_date, price):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO movies (name, type, release_date, price)
        VALUES (?, ?, ?, ?)
    """, (name, genre, release_date, price))

    conn.commit()
    conn.close()


def list_movies():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM movies")
    movies = cursor.fetchall()

    conn.close()
    return movies


def delete_movie(movie_name):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM movies WHERE name = ?", (movie_name,))
    conn.commit()

    if cursor.rowcount == 0:
        print("No movie found with that name.")
    else:
        print("✅ Movie deleted successfully.")

    conn.close()