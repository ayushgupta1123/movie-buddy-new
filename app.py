import ast
import os
import pickle
 
import numpy as np
import pandas as pd
import streamlit as st
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
 
# ---------- Page config ----------
st.set_page_config(
    page_title="Movie Night Buddy",
    page_icon="🎬",
    layout="wide"
)
 
# ---------- Data-building helpers (mirrors the notebook pipeline) ----------
def convert(obj):
    return [i['name'] for i in ast.literal_eval(obj)]
 
 
def convert3(obj):
    L, counter = [], 0
    for i in ast.literal_eval(obj):
        if counter == 3:
            break
        L.append(i['name'])
        counter += 1
    return L
 
 
def fetch_director(obj):
    for i in ast.literal_eval(obj):
        if i['job'] == 'Director':
            return [i['name']]
    return []
 
 
def stem(text, ps=PorterStemmer()):
    return " ".join(ps.stem(i) for i in text.split())
 
 
def build_data():
    """Recreates movies_dict and similarity matrix from the raw CSVs."""
    movies = pd.read_csv('tmdb_5000_movies.csv')
    credits = pd.read_csv('tmdb_5000_credits.csv')
 
    movies = movies.merge(credits, on='title')
    movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]
    movies.dropna(inplace=True)
 
    movies['genres'] = movies['genres'].apply(convert)
    movies['keywords'] = movies['keywords'].apply(convert)
    movies['cast'] = movies['cast'].apply(convert3)
    movies['crew'] = movies['crew'].apply(fetch_director)
    movies['overview'] = movies['overview'].apply(lambda x: x.split())
 
    for col in ['genres', 'keywords', 'cast', 'crew']:
        movies[col] = movies[col].apply(lambda x: [i.replace(" ", "") for i in x])
 
    movies['tags'] = (
        movies['overview'] + movies['genres'] + movies['keywords']
        + movies['cast'] + movies['crew']
    )
 
    new_df = movies[['movie_id', 'title', 'tags']].copy()
    new_df['tags'] = new_df['tags'].apply(lambda x: " ".join(x))
    new_df['tags'] = new_df['tags'].apply(stem)
    new_df['tags'] = new_df['tags'].apply(lambda x: x.lower())
 
    cv = CountVectorizer(max_features=5000, stop_words='english')
    vectors = cv.fit_transform(new_df['tags']).toarray()
    similarity = cosine_similarity(vectors)
 
    return new_df.to_dict(), similarity
 
 
# ---------- Load data ----------
@st.cache_resource
def load_data():
    # Fast path: use pre-built pickles if they exist locally.
    if os.path.exists("movie_dict.pkl") and os.path.exists("similarity.pkl"):
        movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
        movies = pd.DataFrame(movies_dict)
        similarity = pickle.load(open("similarity.pkl", "rb"))
        return movies, similarity
 
    # Fallback: rebuild from the raw CSVs (used on Streamlit Cloud,
    # since the large .pkl files aren't committed to GitHub).
    movies_dict, similarity = build_data()
    movies = pd.DataFrame(movies_dict)
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
st.caption("A content-based movie recommender — pick a film you like and get 5 similar picks.")
 
selected_movie = st.selectbox(
    "Choose a movie",
    movies["title"].values
)
 
if st.button("Recommend"):
    names, scores = recommend(selected_movie)
 
    cols = st.columns(5)
    for col, name, score in zip(cols, names, scores):
        with col:
            st.markdown(f"**{name}**")
            st.caption(f"Match: {score}%")
