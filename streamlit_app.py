import streamlit as st
import pandas as pd
from app.database import get_connection
from analytics.insights import get_movie_popularity_data, get_total_revenue
from analytics.dashboard import generate_dashboard_plot
from ml_engine.recommender import CineBookRecommender

# -----------------------------------------------------
# PAGE CONFIG
# -----------------------------------------------------
st.set_page_config(page_title="CineBook AI", layout="wide")

st.title("🎬 CineBook AI")
st.subheader("Intelligent Movie Booking & Recommendation Platform")

# -----------------------------------------------------
# INITIALIZE RECOMMENDER
# -----------------------------------------------------
if "recommender" not in st.session_state:
    st.session_state.recommender = CineBookRecommender()

recommender = st.session_state.recommender

# -----------------------------------------------------
# SIDEBAR
# -----------------------------------------------------
page = st.sidebar.selectbox(
    "Navigation",
    ["View Movies", "Create Booking", "Analytics Dashboard", "AI Recommendation"]
)

conn = get_connection()

# =====================================================
# 1️⃣ VIEW MOVIES (POSTER GRID)
# =====================================================
if page == "View Movies":

    st.header("🎥 Available Movies")

    movies_df = recommender.movies_df

    cols = st.columns(3)

    for idx, row in movies_df.iterrows():
        with cols[idx % 3]:
            st.image(row["poster_url"], width=300)
            st.markdown(
                f"""
                <div style='height:60px; font-size:22px; font-weight:bold'>
                {row['title']}
                </div>
                """,
                unsafe_allow_html=True
            )
            st.markdown(f"⭐ IMDB: {row['imdb_rating']}")
            st.markdown(f"🎭 {row['genres']}")
            st.markdown(f"📅 {row['year']}")
            st.markdown("---")

# =====================================================
# 2️⃣ CREATE BOOKING (DB BASED)
# =====================================================
elif page == "Create Booking":

    st.header("🎟 Create Booking")

    movies = pd.read_sql("SELECT * FROM movies", conn)

    if movies.empty:
        st.warning("Please add movies first.")
    else:
        selected_movie = st.selectbox("Select Movie", movies["name"].tolist())
        customer_name = st.text_input("Customer Name")
        tickets = st.number_input("Number of Tickets", min_value=1, step=1)

        if st.button("Book Now"):

            price = movies[movies["name"] == selected_movie]["price"].values[0]
            total_cost = price * tickets

            conn.execute(
                "INSERT INTO bookings (customer_name, movie_name, tickets, total_cost) VALUES (?, ?, ?, ?)",
                (customer_name, selected_movie, tickets, total_cost)
            )
            conn.commit()

            st.success(f"✅ Booking Successful! Total Cost: ₹{total_cost}")

# =====================================================
# 3️⃣ ANALYTICS DASHBOARD
# =====================================================
elif page == "Analytics Dashboard":

    st.header("📊 Analytics Dashboard")

    popularity_data = get_movie_popularity_data()
    total_revenue = get_total_revenue()

    if not popularity_data:
        st.warning("No booking data available.")
    else:
        movies = [row[0] for row in popularity_data]
        tickets = [row[1] for row in popularity_data]

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("💰 Total Revenue", f"₹{total_revenue}")

        with col2:
            st.metric("🎟 Total Tickets Sold", sum(tickets))

        with col3:
            st.metric("🔥 Most Popular Movie", movies[0])

        st.divider()

        fig = generate_dashboard_plot()
        st.pyplot(fig)

# =====================================================
# 4️⃣ AI RECOMMENDATION
# =====================================================
elif page == "AI Recommendation":

    st.header("🤖 AI-Powered Recommendation Engine")

    st.subheader("1️⃣ Set Your Preferences")

    action_pref = st.slider("Action Preference", 1, 5, 3)
    drama_pref = st.slider("Drama Preference", 1, 5, 3)
    scifi_pref = st.slider("Sci-Fi Preference", 1, 5, 3)
    nolan_pref = st.slider("Christopher Nolan Preference", 1, 5, 3)

    preferences = {
        "genres": {
            "Action": action_pref,
            "Drama": drama_pref,
            "Sci-Fi": scifi_pref
        },
        "directors": {
            "Christopher Nolan": nolan_pref
        }
    }

    recommender.set_user_preferences(preferences)

    st.divider()

    st.subheader("2️⃣ What Should You Watch Today?")

    genre_choice = st.selectbox(
        "Today's Genre Mood",
        ["Action", "Drama", "Sci-Fi", "Crime", "Adventure"]
    )

    era_options = {
        "Classic (1940-1969)": (1940, 1969),
        "Golden (1970-1989)": (1970, 1989),
        "Modern (1990-2009)": (1990, 2009),
        "Contemporary (2010+)": (2010, 2025)
    }

    era_label = st.selectbox("Preferred Era", list(era_options.keys()))
    era_choice = era_options[era_label]

    if st.button("🎬 Get AI Recommendation"):

        recommendation = recommender.recommend_for_today(
            genre_choice,
            era_choice
        )

        if recommendation:

            movie_row = recommender.movies_df[
                recommender.movies_df["title"] == recommendation
            ].iloc[0]

            st.success(f"🌟 Recommended Movie: {recommendation}")

            st.image(movie_row["poster_url"], width=300)

            st.markdown("### 🎬 Movie Details")
            st.write(f"**Year:** {movie_row['year']}")
            st.write(f"**IMDB Rating:** {movie_row['imdb_rating']}")
            st.write(f"**Director:** {movie_row['director']}")
            st.write(f"**Genres:** {movie_row['genres']}")

        else:
            st.warning("No suitable recommendation found.")