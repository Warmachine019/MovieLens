import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import textwrap

df = pd.read_csv("Datasets/Movie Ratings.csv")
os.makedirs("Graphs", exist_ok=True)

plt.figure(figsize=(7,5))
sns.histplot(df["rating"], bins=9, kde=True, color="skyblue", discrete=True)
plt.title("Ratings Distribution with Density Curve")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("Graphs/histogram_with_curve.png")
plt.close()
movie_stats = df.groupby("title").agg({"rating":"count"}).reset_index()
movie_stats = movie_stats.rename(columns={"rating":"rating_count"})
top_movies = movie_stats.sort_values("rating_count", ascending=False).head(10)

top_movies["title_wrapped"] = top_movies["title"].apply(lambda x: "\n".join(textwrap.wrap(x, 25)))

plt.figure(figsize=(10,6))
sns.barplot(x="rating_count", y="title_wrapped", data=top_movies, color="skyblue")
plt.title("Top 10 Movies by Number of Ratings")
plt.xlabel("Number of Ratings")
plt.ylabel("Movie Title")
plt.tight_layout()
plt.savefig("Graphs/bar_top10_movies.png")
plt.close()
print("Histogram is saved")
