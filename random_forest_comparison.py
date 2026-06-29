import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

df = pd.read_csv("soccer_positions.csv")

df["Position"] = df["Position"].map({
    "Forward":1,
    "Winger":2
})

df["Elite Player"] = (df["Goals"]>25).astype(int)

X = df[["Matches","Assists","Position"]]
y = df["Elite Player"]

logistic_model = LogisticRegression()
logistic_accuracy = cross_val_score(
    logistic_model,
    X,y,
    cv=5,
    scoring="accuracy"
).mean()

tree_model = DecisionTreeClassifier(max_depth=3,random_state=42)
tree_accuracy = cross_val_score(
    tree_model,
    X,y,
    cv=5,
    scoring="accuracy"
).mean()

forest_model = RandomForestClassifier(random_state=42)
forest_accuracy = cross_val_score(
   forest_model,
    X,y,
    cv=5,
    scoring="accuracy"
).mean()

results = {
"Logistic Regression":logistic_accuracy,
"Decision Tree":tree_accuracy,
"Random Forest":forest_accuracy
}

for model,accuracy in results.items():
    print(f"{model}:{accuracy:.3f}")

best_model = max(
    results,
    key=results.get
)

print("Best Model: ", best_model)
print("Highest Accuracy: ", results[best_model])

plt.bar(
    results.keys(),
    results.values()
)
plt.title("Model Comparison")
plt.ylabel("Accuracy")
plt.show()