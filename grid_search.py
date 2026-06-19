import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV

df = pd.read_csv("soccer_positions.csv")

df["Position"] = df["Position"].map({
    "Forward":1,
    "Winger":2
})

df["Elite Player"] = (df["Goals"] > 25).astype(int)

X = df[["Matches", "Assists", "Position"]]
y = df["Elite Player"]

model = DecisionTreeClassifier()

param_grid = {
    "max_depth": [1,2,3,4,5]
}

search = GridSearchCV(
    model,
    param_grid,
    cv=5,
    scoring="accuracy"
)

search.fit(X,y)

print("\nBest Parameter: ")
print(search.best_params_)

print("\nBest Accuracy: ")
print(search.best_score_)