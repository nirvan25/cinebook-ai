from app.database import initialize_db
from app.movies import add_movie, list_movies

def main():
    initialize_db()

    add_movie("Inception", "Sci-Fi", "2010", 250)
    add_movie("Interstellar", "Sci-Fi", "2014", 300)
    add_movie("The Dark Knight", "Action", "2008", 280)

    movies = list_movies()
    print("\n🎬 Movies Available:\n")
    for movie in movies:
        print(movie)

if __name__ == "__main__":
    main()