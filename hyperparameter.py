import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score

df = pd.read_csv("soccer_positions.csv")

df["Position"] = df["Position"].map({
    "Forward":1,
    "Winger":2
})

df["Elite Player"] = (df["Goals"]>25).astype(int)

X = df[["Matches", "Assists", "Position"]]
y = df["Elite Player"]

result = {}

for depth in [1,2,3,4,5]:
    model = DecisionTreeClassifier(
        max_depth=depth,
        random_state=42
    )

    score = cross_val_score(
        model,
        X,y,
        cv=5,
        scoring="accuracy"
    )

    accuracy = score.mean()
    
    result[f"Depth {depth}"] = accuracy

print("Tree Perfomance: ")
for tree, accuracy in result.items():
    print(f"{tree}: {accuracy:.3f}")

best_tree = max(
    result,
    key=result.get
)

print("Best Tree: ", best_tree)
print("Highest Accuracy: ", result[best_tree])

plt.bar(
    result.keys(),
    result.values()
)
plt.title("Decision Tree Depth Comparision")
plt.xlabel("Tree Depth")
plt.ylabel("Average Accuracy Score")
plt.show()