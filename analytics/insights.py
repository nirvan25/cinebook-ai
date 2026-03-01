from app.database import connect


def get_total_revenue():
    """
    Returns total revenue generated from all bookings.
    """
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(total_cost) FROM bookings")
    result = cursor.fetchone()

    conn.close()

    return result[0] if result[0] else 0


def get_most_popular_movie():
    """
    Returns the most popular movie based on total tickets sold.
    """
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT movie_name, SUM(tickets) as total_tickets
        FROM bookings
        GROUP BY movie_name
        ORDER BY total_tickets DESC
        LIMIT 1
    """)

    result = cursor.fetchone()
    conn.close()

    return result


def get_movie_popularity_data():
    """
    Returns all movies with total tickets sold,
    ordered by popularity.
    """
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT movie_name, SUM(tickets) as total_tickets
        FROM bookings
        GROUP BY movie_name
        ORDER BY total_tickets DESC
    """)

    data = cursor.fetchall()
    conn.close()

    return data