import pandas as pd


class CineBookRecommender:

    def __init__(self):

        self.movies_df = pd.DataFrame([

            # ================= CLASSIC (1940–1969) =================
            {
                "title": "Casablanca",
                "year": 1942,
                "genres": "Drama, Romance",
                "director": "Michael Curtiz",
                "imdb_rating": 8.5,
                "poster_url": "https://image.tmdb.org/t/p/w500/5K7cOHoay2mZusSLezBOY0Qxh8a.jpg"
            },
            {
                "title": "Psycho",
                "year": 1960,
                "genres": "Crime, Thriller",
                "director": "Alfred Hitchcock",
                "imdb_rating": 8.5,
                "poster_url": "https://image.tmdb.org/t/p/w500/81d8oyEFgj7FlxJqSDXWr8JH8kV.jpg"
            },

            # ================= GOLDEN (1970–1989) =================
            {
                "title": "The Godfather",
                "year": 1972,
                "genres": "Crime, Drama",
                "director": "Francis Ford Coppola",
                "imdb_rating": 9.2,
                "poster_url": "https://image.tmdb.org/t/p/w500/3bhkrj58Vtu7enYsRolD1fZdja1.jpg"
            },
            {
                "title": "Taxi Driver",
                "year": 1976,
                "genres": "Crime, Drama",
                "director": "Martin Scorsese",
                "imdb_rating": 8.2,
                "poster_url": "https://image.tmdb.org/t/p/w500/ekstpH614fwDX8DUln1a2Opz0N8.jpg"
            },
            {
                "title": "Back to the Future",
                "year": 1985,
                "genres": "Sci-Fi, Adventure",
                "director": "Robert Zemeckis",
                "imdb_rating": 8.5,
                "poster_url": "https://image.tmdb.org/t/p/w500/fNOH9f1aA7XRTzl1sAOx9iF553Q.jpg"
            },

            # ================= MODERN (1990–2009) =================
            {
                "title": "The Shawshank Redemption",
                "year": 1994,
                "genres": "Drama",
                "director": "Frank Darabont",
                "imdb_rating": 9.3,
                "poster_url": "https://image.tmdb.org/t/p/w500/q6y0Go1tsGEsmtFryDOJo3dEmqu.jpg"
            },
            {
                "title": "Fight Club",
                "year": 1999,
                "genres": "Drama",
                "director": "David Fincher",
                "imdb_rating": 8.8,
                "poster_url": "https://image.tmdb.org/t/p/w500/bptfVGEQuv6vDTIMVCHjJ9Dz8PX.jpg"
            },
            {
                "title": "The Dark Knight",
                "year": 2008,
                "genres": "Action, Crime",
                "director": "Christopher Nolan",
                "imdb_rating": 9.0,
                "poster_url": "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg"
            },

            # ================= CONTEMPORARY (2010+) =================
            {
                "title": "Inception",
                "year": 2010,
                "genres": "Sci-Fi, Action",
                "director": "Christopher Nolan",
                "imdb_rating": 8.8,
                "poster_url": "https://image.tmdb.org/t/p/w500/8IB2e4r4oVhHnANbnm7O3Tj6tF8.jpg"
            },
            {
                "title": "Student of the Year",
                "year": 2012,
                "genres": "Drama, Romance",
                "director": "Karan Johar",
                "imdb_rating": 5.2,
                "poster_url": "assets/student_of_the_year.jpg"
            },
            {
                "title": "Interstellar",
                "year": 2014,
                "genres": "Sci-Fi, Drama",
                "director": "Christopher Nolan",
                "imdb_rating": 8.6,
                "poster_url": "https://image.tmdb.org/t/p/w500/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg"
            },
            {
                "title": "Avengers Endgame",
                "year": 2019,
                "genres": "Action, Adventure",
                "director": "Anthony Russo",
                "imdb_rating": 8.4,
                "poster_url": "https://image.tmdb.org/t/p/w500/or06FN3Dka5tukK1e9sl16pB3iy.jpg"
            },
            {
                "title": "Joker",
                "year": 2019,
                "genres": "Crime, Drama",
                "director": "Todd Phillips",
                "imdb_rating": 8.4,
                "poster_url": "https://image.tmdb.org/t/p/w500/udDclJoHjfjb8Ekgsd4FDteOkCU.jpg"
            },
            {
                "title": "Parasite",
                "year": 2019,
                "genres": "Thriller, Drama",
                "director": "Bong Joon-ho",
                "imdb_rating": 8.5,
                "poster_url": "https://image.tmdb.org/t/p/w500/7IiTTgloJzvGI1TAYymCfbfl3vT.jpg"
            }
        ])

        self.movies_df["year"] = self.movies_df["year"].astype(int)
        self.movies_df["imdb_rating"] = self.movies_df["imdb_rating"].astype(float)

        self.user_preferences = {}

    def set_user_preferences(self, preferences):
        self.user_preferences = preferences

    def recommend_for_today(self, genre_choice, era_range):

        start_year = int(era_range[0])
        end_year = int(era_range[1])

        filtered = self.movies_df[
            (self.movies_df["year"] >= start_year) &
            (self.movies_df["year"] <= end_year)
        ]

        filtered = filtered[
            filtered["genres"].str.contains(genre_choice, case=False)
        ]

        if filtered.empty:
            return None

        filtered = filtered.copy()
        filtered["score"] = filtered["imdb_rating"]

        director_prefs = self.user_preferences.get("directors", {})
        for director, weight in director_prefs.items():
            filtered.loc[
                filtered["director"] == director,
                "score"
            ] += weight * 0.5

        genre_prefs = self.user_preferences.get("genres", {})
        for genre, weight in genre_prefs.items():
            filtered.loc[
                filtered["genres"].str.contains(genre, case=False),
                "score"
            ] += weight * 0.3

        best_movie = filtered.sort_values(by="score", ascending=False).iloc[0]
        return best_movie["title"]