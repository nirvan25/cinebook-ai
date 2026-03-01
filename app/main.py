from app.database import initialize_db
from app.movies import add_movie, list_movies

def main():
    initialize_db()

    add_movie("Inception", "Sci-Fi", "2010", 250)

    movies = list_movies()
    print(movies)

if __name__ == "__main__":
    main()