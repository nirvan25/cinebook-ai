import matplotlib.pyplot as plt
from analytics.insights import get_movie_popularity_data, get_total_revenue


def show_dashboard():
    popularity_data = get_movie_popularity_data()
    revenue = get_total_revenue()

    if not popularity_data:
        print("No booking data available for visualization.")
        return

    movies = [row[0] for row in popularity_data]
    tickets = [row[1] for row in popularity_data]

    plt.figure(figsize=(10, 6))
    bars = plt.bar(movies, tickets)

    plt.xlabel("Movies")
    plt.ylabel("Tickets Sold")
    plt.title(f"Movie Popularity | Total Revenue ₹{revenue}")
    plt.xticks(rotation=30)
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"{int(height)}",
            ha="center",
            va="bottom"
        )

    plt.tight_layout()
    plt.show()