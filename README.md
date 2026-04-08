# MovieLens
A genre based movie recommender system.

The system uses the MovieLens dataset from kaggle.

📖 How it Works
Data Merging: Since tags.csv has multiple rows per movie, we use groupby to concatenate all tags for a single movieId into one string.

Preprocessing: We strip out years (like "(1995)"), punctuation, and common words (the, is, at) that don't help in distinguishing one movie from another.

TF-IDF Vectorization:

TF (Term Frequency): How often a word appears in a movie's tags.

IDF (Inverse Document Frequency): Reduces the weight of words that appear in every movie (like "film" or "story"), making unique tags more important.

Bigrams: By setting ngram_range=(1, 2), the model understands "science fiction" as a single unit rather than just "science" and "fiction" separately.

Cosine Similarity: This calculates the "angle" between two movie vectors. If the vectors point in a similar direction, the movies share similar descriptive keywords.

🚀 Running the Project
Place movies.csv and tags.csv in the data/ folder.

Run the script:

Bash
python main.py
Type a movie name (e.g., "Toy Story" or "Inception") when prompted.
