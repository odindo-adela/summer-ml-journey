import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt

df = pd.read_csv("soccer_positions.csv")

df["Position"] = df["Position"].map({
     "Forward":1,
     "Winger":2
}
)
X = df[["Matches", "Position"]]
y = df["Goals"]

linear_model = LinearRegression()
linear_scores = cross_val_score(
    linear_model,
    X,y,
    cv=5,
    scoring="neg_mean_absolute_error"
)
linear_mae = (-linear_scores).mean()
print("\nLinear Regression MAE: ", linear_mae)

tree_model = DecisionTreeRegressor(random_state=42)
tree_scores = cross_val_score(
    tree_model,
    X,y,
    cv=5,
    scoring="neg_mean_absolute_error"
)
tree_mae = (-tree_scores).mean()
print("\nDecision Tree MAE: ", tree_mae)

if linear_mae<tree_mae:
    print("\nLinear Model wins!")
else:
    print("\nDecision Tree Model wins!")

plt.bar(
    ["Linear Regression", "Decision Tree"],
    [linear_mae, tree_mae]
)
plt.title("Model Comparision")
plt.ylabel("Average MAE")
plt.show()