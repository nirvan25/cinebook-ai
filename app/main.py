from app.database import initialize_db
from analytics.dashboard import show_dashboard
from analytics.insights import recommend_movie

def main():
    initialize_db()

    recommendation = recommend_movie()

    if recommendation:
        print(f"\n🤖 Recommended Movie Based on Trends: {recommendation}")
    else:
        print("No recommendation available yet.")

    show_dashboard()

if __name__ == "__main__":
    main()