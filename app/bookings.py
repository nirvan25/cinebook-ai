import sqlite3

DATABASE_PATH = "database/cinebook.db"


def create_booking(customer_name, mobile, movie_name, tickets, seat_type, show_time):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT price FROM movies WHERE name = ?", (movie_name,))
    result = cursor.fetchone()

    if not result:
        print("Movie not found.")
        conn.close()
        return

    price = result[0]

    if seat_type.lower() == "premium":
        multiplier = 1.5
    elif seat_type.lower() == "vip":
        multiplier = 2
    else:
        multiplier = 1

    total_cost = price * tickets * multiplier

    cursor.execute("""
        INSERT INTO bookings
        (customer_name, mobile, movie_name, tickets, seat_type, total_cost, show_time)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (customer_name, mobile, movie_name, tickets, seat_type, total_cost, show_time))

    conn.commit()
    conn.close()

    print(f"✅ Booking successful! Total cost: ₹{total_cost}")