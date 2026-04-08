# 🎬 MovieLens: NLP-Powered Movie Recommender

CinemaMatch is a content-based recommendation system that uses Natural Language Processing (NLP) to suggest movies. By analyzing titles and genres from the MovieLens dataset, the engine identifies mathematical similarities between films to provide relevant suggestions.

---

## 🚀 Key Features
- **Smart Text Cleaning**: Automated removal of release years, special characters, and "noise" words (stopwords).
- **TF-IDF Vectorization**: Uses Term Frequency-Inverse Document Frequency to identify which genres and keywords define a movie's identity.
- **Bi-gram Analysis**: The engine recognizes two-word phrases (like "Sci-Fi" or "Film Noir") for better accuracy.
- **Glassmorphism UI**: A modern, dark-themed web interface built with Flask and custom CSS.

---

## 🛠️ Technical Stack
- **Backend**: Python, Flask
- **Data Handling**: Pandas, NumPy
- **NLP & ML**: NLTK (Natural Language Toolkit), Scikit-learn
- **Frontend**: HTML5, CSS3 (Glassmorphism design)

---

## 🧠 How It Works

The recommendation engine follows a four-step NLP pipeline:

1. **Preprocessing**: 
   Raw text is converted to lowercase, stripped of punctuation, and "lemmatized" (converting words like *Incredibles* to *Incredible*).
   
2. **Vectorization**: 
   The `TfidfVectorizer` converts the cleaned text into a sparse matrix of numerical values. It assigns higher weights to unique genres and lower weights to very common words.
   
3. **Similarity Calculation**: 
   When a user searches for a movie, the system calculates the **Cosine Similarity** between that movie's vector and all other 27,000+ movies in the dataset.
   
4. **Ranking**: 
   The system sorts the results and returns the top 5 movies with the highest similarity score (closest to 1.0).



---

## 📂 Project Structure
```text
movie_recommender/
├── app.py              # Flask Server & NLP Engine
├── movies.csv          # MovieLens Dataset
├── static/
│   └── style.css       # Custom UI Styling
├── templates/
│   └── index.html      # Web Layout
└── requirements.txt    # Project Dependencies
