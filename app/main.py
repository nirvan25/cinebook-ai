from app.database import initialize_db
from app.bookings import create_booking

def main():
    initialize_db()

    create_booking(
        customer_name="Nirvan",
        mobile="9999999999",
        movie_name="Inception",
        tickets=3,
        seat_type="VIP",
        show_time="7 PM"
    )

if __name__ == "__main__":
    main()