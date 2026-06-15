import pandas as pd
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt


df = pd.read_csv("soccer_positions.csv")

df["Position"] = df["Position"].map({
    "Forward":1,
    "Winger":2
})

X = df[["Matches", "Assists", "Position"]]
y = df["Goals"]

model = DecisionTreeRegressor(
    max_depth=3,
    random_state=42
)

model.fit(X,y)

print(model.feature_importances_)

for feature, importance in zip(
    X.columns,
    model.feature_importances_
):
    print(
        feature,
        ":",
        importance
    )

importance_dict = {}
for feature, importance in zip(
    X.columns,
    model.feature_importances_
):
    importance_dict[feature] = importance

most_important = max(
    importance_dict,
    key=importance_dict.get
)

print("Most Important Feature:", most_important)
print("Importance Score: ", importance_dict[most_important])

plt.bar(
    X.columns,
    model.feature_importances_
)
plt.title("Feature Importance")
plt.ylabel("Importance")
plt.show()