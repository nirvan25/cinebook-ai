from app.database import initialize_db
from app.movies import list_movies, add_movie
from app.bookings import create_booking
from analytics.dashboard import show_dashboard
from analytics.insights import recommend_movie


def display_movies():
    movies = list_movies()

    if not movies:
        print("\nNo movies available.")
        return

    print("\n🎬 Available Movies:")
    for movie in movies:
        # movie structure: (id, name, type, release_date, price)
        print(f"{movie[1]} | ₹{movie[4]}")


def main():
    initialize_db()

    while True:
        print("\n===== 🎬 CineBook AI =====")
        print("1. View Movies")
        print("2. Create Booking")
        print("3. View Analytics Dashboard")
        print("4. Get Recommended Movie")
        print("5. Add Movie")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            display_movies()

        elif choice == "2":
            name = input("Customer Name: ")
            mobile = input("Mobile: ")
            movie = input("Movie Name: ")
            tickets = int(input("Number of Tickets: "))
            seat = input("Seat Type (Standard/Premium/VIP): ")
            show_time = input("Show Time: ")

            create_booking(name, mobile, movie, tickets, seat, show_time)

        elif choice == "3":
            show_dashboard()

        elif choice == "4":
            rec = recommend_movie()
            if rec:
                print(f"\n🤖 Recommended Movie: {rec}")
            else:
                print("\nNo recommendation available yet.")

        elif choice == "5":
            name = input("Movie Name: ")
            genre = input("Genre: ")
            release = input("Release Year: ")
            price = float(input("Ticket Price: "))

            add_movie(name, genre, release, price)
            print("✅ Movie added successfully.")

        elif choice == "6":
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()