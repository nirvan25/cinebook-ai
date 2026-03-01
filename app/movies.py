from app.database import connect

def add_movie(name, type_, release_date, price):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO movies (name, type, release_date, price)
        VALUES (?, ?, ?, ?)
    """, (name, type_, release_date, price))
    conn.commit()
    conn.close()
    print("✅ Movie added successfully!")

def list_movies():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM movies")
    movies = cursor.fetchall()
    conn.close()
    return movies