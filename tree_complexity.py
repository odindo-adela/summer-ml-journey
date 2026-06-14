import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import cross_val_score

# Load data
df = pd.read_csv("soccer_positions.csv")

df["Position"] = df["Position"].map({
    "Forward": 1,
    "Winger": 2
})

# Features and target
X = df[["Matches", "Position"]]
y = df["Goals"]

# Store results
results = {}

# Test different tree depths
for depth in [1, 2, 3, 4]:

    model = DecisionTreeRegressor(
        max_depth=depth,
        random_state=42
    )

    scores = cross_val_score(
        model,
        X,
        y,
        cv=5,
        scoring="neg_mean_absolute_error"
    )

    mae = (-scores).mean()

    results[f"Depth {depth}"] = mae

# Unlimited depth tree
unlimited_model = DecisionTreeRegressor(
    random_state=42
)

scores = cross_val_score(
    unlimited_model,
    X,
    y,
    cv=5,
    scoring="neg_mean_absolute_error"
)

unlimited_mae = (-scores).mean()

results["Unlimited"] = unlimited_mae

# Print results
print("Tree Performance:")

for tree, mae in results.items():
    print(f"{tree}: {mae:.3f}")

# Find best tree
best_tree = min(
    results,
    key=results.get
)

print("\nBest Tree:", best_tree)
print("Best MAE:", results[best_tree])

# Visualization
plt.bar(
    results.keys(),
    results.values()
)

plt.title("Decision Tree Depth Comparison")
plt.xlabel("Tree Depth")
plt.ylabel("Average MAE")

plt.show()