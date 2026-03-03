import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load dataset
df = pd.read_csv("Datasets/Movie Ratings.csv")

# Create Graphs folder if not exists
os.makedirs("Graphs", exist_ok=True)

# Count frequency of each rating value
rating_counts = df["rating"].value_counts().reset_index()
rating_counts.columns = ["rating", "count"]

# Sort descending by count
rating_counts = rating_counts.sort_values("count", ascending=False)

# Plot (highest to lowest, no gaps)
plt.figure(figsize=(8,6))
sns.barplot(
    x="rating",
    y="count",
    data=rating_counts,
    order=rating_counts["rating"],  # ensures highest → lowest
    color="skyblue"
)

plt.title("Ratings Frequency (Highest to Lowest)")
plt.xlabel("Rating Value")
plt.ylabel("Count of Ratings")

# Remove gaps between bars
plt.gca().set_xlim(-0.5, len(rating_counts)-0.5)

plt.tight_layout()
plt.savefig("Graphs/bar_ratings_highest_to_lowest.png")
plt.close()

print("✅ Bar graph saved in Graphs/ (Ratings frequency, highest → lowest, no gaps)")
