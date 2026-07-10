import pickle
import pandas as pd
import streamlit as st

# ---------- Page config ----------
st.set_page_config(
    page_title="Movie Night Buddy 🎬",
    page_icon="🎬",
    layout="wide",
)

# ---------- Load data ----------
@st.cache_data
def load_data():
    movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
    movies = pd.DataFrame(movies_dict)
    similarity = pickle.load(open("similarity.pkl", "rb"))
    return movies, similarity

movies, similarity = load_data()

# ---------- Recommend logic ----------
def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(
        list(enumerate(distances)), reverse=True, key=lambda x: x[1]
    )[1:6]

    names, scores = [], []
    for i in movies_list:
        names.append(movies.iloc[i[0]].title)
        scores.append(round(i[1] * 100, 1))
    return names, scores

# ---------- UI ----------
st.title("🎬 Movie Night Buddy")
st.caption("A content-based movie recommender — pick a film you like, get 5 similar picks.")

col1, col2 = st.columns([3, 1])
with col1:
    selected_movie = st.selectbox(
        "Search for a movie you enjoyed:",
        movies["title"].values,
        index=None,
        placeholder="Start typing a movie name...",
    )
with col2:
    st.write("")
    st.write("")
    recommend_clicked = st.button("🎯 Recommend", use_container_width=True)

if recommend_clicked and selected_movie:
    with st.spinner("Finding movies you'll love..."):
        names, scores = recommend(selected_movie)

    st.subheader(f"Because you liked *{selected_movie}*")
    for rank, (name, score) in enumerate(zip(names, scores), start=1):
        col1, col2 = st.columns([5, 1])
        with col1:
            st.markdown(f"**{rank}. {name}**")
            st.progress(min(score / 100, 1.0))
        with col2:
            st.metric(label="Match", value=f"{score}%")

elif recommend_clicked and not selected_movie:
    st.warning("Pick a movie first 🙂")

with st.expander("ℹ️ How this works"):
    st.write(
        "Each movie is represented as a 'tag' made of its overview, genres, "
        "keywords, cast, and crew. Text is stemmed and vectorized with "
        "CountVectorizer (bag-of-words, top 5000 features), then movies are "
        "compared using cosine similarity. The 5 closest movies to your pick "
        "are recommended."
    )
    