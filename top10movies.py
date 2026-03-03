import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import textwrap

# Load dataset
df = pd.read_csv("Datasets/Movie Ratings.csv")

# Create Graphs folder if not exists
os.makedirs("Graphs", exist_ok=True)

# =========================
# Top 10 Movies by Rating Count (Vertical Bar Chart)
# =========================
movie_stats = df.groupby("title").agg({"rating":"count"}).reset_index()
movie_stats = movie_stats.rename(columns={"rating":"rating_count"})
top_movies = movie_stats.sort_values("rating_count", ascending=False).head(10)

# Wrap long titles
top_movies["title_wrapped"] = top_movies["title"].apply(lambda x: "\n".join(textwrap.wrap(x, 20)))

plt.figure(figsize=(10,6))
sns.barplot(x="title_wrapped", y="rating_count", data=top_movies, color="skyblue")
plt.title("Top 10 Movies by Number of Ratings")
plt.xlabel("Movie Title")
plt.ylabel("Number of Ratings")
plt.xticks(rotation=45, ha="right")  # rotate x labels for readability
plt.tight_layout()
plt.savefig("Graphs/bar_top10_movies_vertical.png")
plt.close()

print("✅ Vertical Top 10 Movies bar chart saved in Graphs/")
