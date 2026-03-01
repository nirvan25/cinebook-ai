import sqlite3

DATABASE_PATH = "database/cinebook.db"


def get_movie_popularity_data():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT movie_name, SUM(tickets)
        FROM bookings
        GROUP BY movie_name
        ORDER BY SUM(tickets) DESC
    """)

    data = cursor.fetchall()
    conn.close()
    return data


def get_total_revenue():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(total_cost) FROM bookings")
    result = cursor.fetchone()

    conn.close()
    return result[0] if result[0] else 0


def recommend_movie():
    data = get_movie_popularity_data()
    if data:
        return data[0][0]
    return None