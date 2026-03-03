# Save this as histogram_lowess.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Requires: statsmodels
from statsmodels.nonparametric.smoothers_lowess import lowess

df = pd.read_csv("Datasets/Movie Ratings.csv")
ratings = df["rating"].dropna().astype(float)

os.makedirs("Graphs", exist_ok=True)

counts = ratings.value_counts().sort_index()
x = counts.index.to_numpy(dtype=float)
y = counts.values.astype(float)

# lowess smoothing (frac controls the smoothness: 0.2-0.6 typical)
frac = 0.35
lowess_res = lowess(y, x, frac=frac, return_sorted=True)
x_lowess = lowess_res[:,0]
y_lowess = lowess_res[:,1]

# interpolate lowess result to dense grid for smooth curve
x_dense = np.linspace(x.min(), x.max(), 800)
y_dense = np.interp(x_dense, x_lowess, y_lowess)

plt.figure(figsize=(8,5))
plt.bar(x, y, width=0.45, color="skyblue", edgecolor="black", alpha=0.9)
plt.plot(x_dense, y_dense, color="red", linewidth=2)
plt.scatter(x, y, color="darkred", s=20)
plt.title(f"Ratings Distribution with LOWESS (frac={frac})")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.xticks(x)
plt.tight_layout()
plt.savefig("Graphs/histogram_lowess.png", dpi=150)
plt.close()

print("✅ Saved: Graphs/histogram_lowess.png")

