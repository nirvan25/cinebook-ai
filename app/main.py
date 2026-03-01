from app.database import initialize_db
from analytics.dashboard import show_dashboard

def main():
    initialize_db()
    show_dashboard()

if __name__ == "__main__":
    main()