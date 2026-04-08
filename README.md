# 🎬 Genre-Based Movie Recommender System

A simple NLP-based movie recommendation system built using the **MovieLens dataset**.
This project uses text analysis techniques like **TF-IDF** and **cosine similarity** to recommend movies based on user-generated tags.

---

## 📌 Overview

This system analyzes movie tags and suggests similar movies based on textual similarity.
It demonstrates core Natural Language Processing (NLP) concepts in a simple and practical way.

---

## ⚙️ How It Works

### 🧩 Data Merging

* The `tags.csv` file contains multiple rows per movie.
* We use **groupby** to combine all tags for each `movieId` into a single string.

---

### 🧹 Text Preprocessing

* Remove years from titles (e.g., `(1995)`)
* Convert text to lowercase
* Remove punctuation
* Remove stopwords (e.g., *the, is, at*)

---

### 📊 TF-IDF Vectorization

* **TF (Term Frequency):** Measures how often a word appears in a movie's tags
* **IDF (Inverse Document Frequency):** Reduces importance of common words

👉 This helps highlight meaningful and unique words.

---

### 🔗 Bigrams

* Using `ngram_range=(1,2)`
* Captures phrases like:

  * "science fiction"
  * "romantic comedy"

---

### 📐 Cosine Similarity

* Measures similarity between movies based on tag vectors
* Movies with similar tags → higher similarity score

---

## 🚀 Running the Project

### 📁 Step 1: Setup

Place the dataset files inside a `data/` folder:

* `movies.csv`
* `tags.csv`

---

### ▶️ Step 2: Run the Script

```bash
python main.py
```

---

### 🎯 Step 3: Input Movie Name

Example:

```
Enter a movie name: Toy Story
```

---

### ✅ Output Example

```
Top 5 Recommended Movies:
1. Finding Nemo
2. Monsters Inc
3. Toy Story 2
4. Cars
5. Shrek
```

---

## 📦 Requirements

Install required libraries:

```bash
pip install pandas scikit-learn nltk
```

---

## 📁 Project Structure

```
movie-recommender/
│── data/
│   ├── movies.csv
│   ├── tags.csv
│
│── src/
│   ├── preprocess.py
│   ├── recommender.py
│
│── main.py
│── README.md
```

---

## 🧠 NLP Concepts Used

* Tokenization
* Stopword Removal
* TF-IDF Vectorization
* N-grams (Bigrams)
* Cosine Similarity

---

## 💡 Future Improvements

* Add Word2Vec or embeddings
* Build a web interface (Streamlit)
* Improve recommendation accuracy using hybrid models

---

## 👨‍💻 Author

Spandan Sahai
