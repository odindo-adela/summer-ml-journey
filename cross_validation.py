from sklearn.model_selection import cross_val_score
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

df = pd.read_csv("soccer_positions.csv")

df["Position"]= df["Position"].map({
    "Forward":1,
    "Winger":2
})

X = df[["Matches", "Position"]]
y = df["Goals"]

model = LinearRegression()

scores = cross_val_score(
    model,
    X,y,
    cv=5,
    scoring="neg_mean_absolute_error"
)

print(scores)

mae_scores = -scores
print("\nMAE Scores: ", mae_scores)

average_mae = mae_scores.mean()
print("\nAverage MAE: ", average_mae)

print("\nBest Fold: ", mae_scores.min())
print("\nWorst Fold: ", mae_scores.max())

plt.bar(
    ["Fold 1", "Fold 2", "Fold 3", "Fold 4", "Fold 5"],
    mae_scores
)
plt.title("Cross Validation MAE")
plt.ylabel("MAE")
plt.show()