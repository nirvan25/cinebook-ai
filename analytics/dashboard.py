import matplotlib.pyplot as plt
from analytics.insights import get_movie_popularity_data, get_total_revenue


def generate_dashboard_plot():
    data = get_movie_popularity_data()

    movies = [row[0] for row in data]
    tickets = [row[1] for row in data]
    total_revenue = get_total_revenue()

    fig, ax = plt.subplots(figsize=(10, 5))

    bars = ax.bar(movies, tickets)

    ax.set_title(f"Movie Popularity | Total Revenue ₹{total_revenue}", fontsize=14)
    ax.set_xlabel("Movies")
    ax.set_ylabel("Tickets Sold")

    ax.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=30)

    # Add numbers on bars
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}',
                ha='center', va='bottom')

    return fig