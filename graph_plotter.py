import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# =========================
# Load dataset
# =========================
df = pd.read_csv("Datasets/Movie Ratings.csv")

# Make sure timestamp is parsed correctly
df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

# Create folder for graphs
os.makedirs("Graphs", exist_ok=True)

# =========================
# 1. Basic Statistics
# =========================
stats = df.describe(include="all")
stats.to_csv("Graphs/basic_statistics.csv")
print("Basic statistics saved as CSV.")

# =========================
# 2. Histogram of Ratings
# =========================
plt.figure(figsize=(6,4))
plt.hist(df["rating"], bins=9, edgecolor="black")
plt.title("Ratings Distribution")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.savefig("Graphs/histogram_ratings.png")
plt.close()

# =========================
# 3. Boxplot of Ratings by Genre (first genre only)
# =========================
df["main_genre"] = df["genres"].apply(lambda x: x.split("|")[0] if isinstance(x, str) else "Unknown")

plt.figure(figsize=(10,6))
sns.boxplot(x="main_genre", y="rating", data=df)
plt.xticks(rotation=90)
plt.title("Ratings by Genre (Boxplot)")
plt.savefig("Graphs/boxplot_ratings_genre.png")
plt.close()

# =========================
# 4. Bar Chart: Average Rating per Genre
# =========================
avg_ratings = df.groupby("main_genre")["rating"].mean().sort_values()

plt.figure(figsize=(8,6))
avg_ratings.plot(kind="barh", color="skyblue")
plt.title("Average Rating per Genre")
plt.xlabel("Average Rating")
plt.savefig("Graphs/bar_avg_rating_genre.png")
plt.close()

# =========================
# 5. Line Chart: Ratings Over Time (per year)
# =========================
ratings_by_year = df.groupby("year")["rating"].mean()

plt.figure(figsize=(8,5))
ratings_by_year.plot(kind="line", marker="o")
plt.title("Average Rating per Year")
plt.xlabel("Year")
plt.ylabel("Average Rating")
plt.savefig("Graphs/line_ratings_year.png")
plt.close()

# =========================
# 6. Scatter Plot: Year vs Rating
# =========================
plt.figure(figsize=(8,5))
plt.scatter(df["year"], df["rating"], alpha=0.05)
plt.title("Scatter Plot: Year vs Rating")
plt.xlabel("Year")
plt.ylabel("Rating")
plt.savefig("Graphs/scatter_year_rating.png")
plt.close()

# =========================
# 7. Correlation Matrix
# =========================
plt.figure(figsize=(6,5))
corr = df[["userId","movieId","rating","year","month"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix")
plt.savefig("Graphs/correlation_matrix.png")
plt.close()

# =========================
# 8. Pie Chart: Genre Distribution
# =========================
genre_counts = df["main_genre"].value_counts().head(10)  # top 10 genres for clarity

plt.figure(figsize=(7,7))
genre_counts.plot(kind="pie", autopct="%1.1f%%")
plt.title("Top 10 Genres Distribution")
plt.ylabel("")
plt.savefig("Graphs/pie_genre_distribution.png")
plt.close()

print("✅ All charts saved in the 'Graphs' folder!")
