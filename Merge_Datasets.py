import pandas as pd

# Load datasets
ratings = pd.read_csv("Datasets/rating.csv")
movies = pd.read_csv("Datasets/movie.csv")

# Merge on movieId
merged = pd.merge(ratings, movies, on="movieId")

# Convert timestamp (already looks like a datetime string, so no unit="s")
merged["timestamp"] = pd.to_datetime(merged["timestamp"], errors="coerce")

# Extract year and month
merged["year"] = merged["timestamp"].dt.year
merged["month"] = merged["timestamp"].dt.month

# Save merged file
merged.to_csv("Movie Ratings.csv", index=False)

print("Final dataset savedMovie Ratings.csv")
print(merged.head())
