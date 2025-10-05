import streamlit as st
import pickle
import pandas as pd


# ---------- Functions ----------
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


# ---------- Data ----------
movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# ---------- Streamlit Layout ----------
st.set_page_config(page_title="🎬 Movie Recommender", page_icon="🎥", layout="wide")

st.title("🎬 Movie Recommender System 🍿")
st.markdown("Find movies you'll love! ❤️", unsafe_allow_html=True)

selected_movie_name = st.selectbox(
    'Select a movie to get recommendations:',
    movies['title'].values
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)

    st.markdown("---")
    st.subheader("Recommended Movies:")

    for idx, movie in enumerate(recommendations, start=1):
        st.markdown(
            f"""
            <div style="
                background: #ffd6e0;
                padding: 20px;
                border-radius: 15px;
                margin-bottom: 10px;
                text-align: center;
                font-weight: bold;
                color: #6a0572;
            ">
                🎬 {movie}
            </div>
            """,
            unsafe_allow_html=True
        )
