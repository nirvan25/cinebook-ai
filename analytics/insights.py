from app.database import get_connection


def get_movie_popularity_data():
    conn = get_connection()
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
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(total_cost) FROM bookings")
    result = cursor.fetchone()[0]

    conn.close()
    return result if result else 0