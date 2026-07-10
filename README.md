# 🎬 Movie Buddy

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-green?style=for-the-badge)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikitlearn)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-black?style=for-the-badge&logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-blue?style=for-the-badge&logo=numpy)

## 🎥 Overview

Movie Buddy is an intelligent **Content-Based Movie Recommendation System** that helps users discover movies similar to their favorites. The application analyzes movie features such as genres, keywords, cast, crew, and overview to recommend the most relevant titles.

The project combines **Machine Learning**, **Natural Language Processing (NLP)**, and an interactive **Streamlit** interface to provide fast and personalized movie recommendations.

---

## ✨ Features

- 🎬 Search from thousands of movies
- 🤖 AI-powered content-based recommendations
- ⭐ Top 5 similar movie suggestions
- 📊 Fast similarity search using cosine similarity
- 🎨 Clean and responsive Streamlit interface
- ⚡ Real-time recommendations
- 🧠 NLP-based feature engineering
- 💻 Beginner-friendly and easy to run

---

## 🖥️ Demo

Simply select a movie from the dropdown list and click the **Recommend** button.

The application instantly displays:

- Recommended movie titles
- Movie posters (if integrated)
- Top 5 similar movies

---

## 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Pandas | Data Processing |
| NumPy | Numerical Computing |
| Scikit-Learn | Machine Learning |
| NLTK | Text Preprocessing |
| Streamlit | Web Application |
| Pickle | Model Serialization |

---

## 📂 Project Structure

```
Movie-Buddy/
│
├── app.py
├── requirements.txt
├── movie_dict.pkl
├── similarity.pkl
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
├── notebook.ipynb
├── assets/
│   └── screenshots/
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/movie-buddy.git
```

### 2️⃣ Navigate

```bash
cd movie-buddy
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Application

```bash
streamlit run app.py
```

---

## 🧠 Machine Learning Workflow

1. Dataset Collection
2. Data Cleaning
3. Feature Engineering
4. Text Preprocessing
5. Tag Creation
6. Vectorization
7. Cosine Similarity Calculation
8. Recommendation Generation
9. Streamlit Deployment

---

## 📊 Recommendation Pipeline

```
Movie Selected
        │
        ▼
Extract Movie Index
        │
        ▼
Similarity Matrix
        │
        ▼
Sort Similar Movies
        │
        ▼
Top 5 Recommendations
        │
        ▼
Display Results
```

---

## 📈 Dataset

The project uses the **TMDB Movie Dataset**, containing information such as:

- Movie Title
- Genres
- Overview
- Keywords
- Cast
- Crew
- Popularity
- Ratings

These features are combined to build meaningful movie representations for recommendation.

---

## 🎯 Recommendation Technique

This project uses a **Content-Based Filtering** approach.

The recommendation engine compares movies based on their textual features instead of relying on user ratings.

The similarity between movies is computed using **Cosine Similarity**, ensuring accurate recommendations based on movie content.

---

## 🚀 Future Improvements

- User authentication
- Collaborative filtering
- Hybrid recommendation system
- Movie trailer integration
- Watchlist functionality
- Genre-wise recommendations
- Mood-based recommendations
- Responsive mobile UI
- Dark mode
- Cloud deployment

---

## 💡 Learning Outcomes

This project helped strengthen knowledge in:

- Machine Learning
- Natural Language Processing
- Data Preprocessing
- Feature Engineering
- Cosine Similarity
- Streamlit Development
- Python Programming
- Model Deployment
- Git & GitHub

---

## 📌 Requirements

```
Python 3.10+

Streamlit

Pandas

NumPy

Scikit-learn

NLTK
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

Feel free to fork the repository and submit a pull request.

---

## 👨‍💻 Author

**Ayush Gupta**

Artificial Intelligence & Machine Learning Engineer

- Python Developer
- Machine Learning Enthusiast
- Data Science Learner

---

## ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub.

It motivates further development and improvements.

---

## 📄 License

This project is intended for educational and learning purposes.

---

### ⭐ "Helping users discover their next favorite movie through Machine Learning."
