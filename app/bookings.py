from app.database import connect
from app.movies import get_movie_price

def calculate_total(movie_name, tickets, seat_type):
    base_price = get_movie_price(movie_name)

    if base_price is None:
        return None

    # Seat type pricing multiplier
    seat_type = seat_type.lower()

    if seat_type == "standard":
        multiplier = 1
    elif seat_type == "premium":
        multiplier = 1.5
    elif seat_type == "vip":
        multiplier = 2
    else:
        multiplier = 1

    return base_price * tickets * multiplier


def create_booking(customer_name, mobile, movie_name, tickets, seat_type, show_time):
    total_cost = calculate_total(movie_name, tickets, seat_type)

    if total_cost is None:
        print("❌ Movie not found.")
        return

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO bookings 
        (customer_name, mobile, movie_name, tickets, seat_type, total_cost, show_time)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (customer_name, mobile, movie_name, tickets, seat_type, total_cost, show_time))

    conn.commit()
    conn.close()

    print(f"✅ Booking successful! Total Cost: ₹{total_cost}")