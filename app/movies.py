from app.database import connect

def add_movie(name, genre, release_date, price):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO movies (name, type, release_date, price)
        VALUES (?, ?, ?, ?)
    """, (name, genre, release_date, price))

    conn.commit()
    conn.close()

def list_movies():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM movies")
    movies = cursor.fetchall()

    conn.close()
    return movies

def get_movie_price(movie_name):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT price FROM movies WHERE name = ?", (movie_name,))
    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]
    return None