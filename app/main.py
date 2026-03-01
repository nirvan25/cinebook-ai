from app.database import initialize_db
from analytics.insights import get_total_revenue, get_most_popular_movie

def main():
    initialize_db()

    revenue = get_total_revenue()
    popular = get_most_popular_movie()

    print(f"\n💰 Total Revenue: ₹{revenue}")

    if popular:
        print(f"🔥 Most Popular Movie: {popular[0]} ({popular[1]} tickets sold)")
    else:
        print("No bookings yet.")

if __name__ == "__main__":
    main()