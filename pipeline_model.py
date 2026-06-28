import pandas as pd
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

df = pd.read_csv("soccer_positions.csv")

df["Position"] = df["Position"].map({
    "Forward":1,
    "Winger":2
})

df["Elite Player"] = (df["Goals"]>25).astype(int)

X = df[["Matches","Assists","Position"]]
y = df["Elite Player"]

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression())
])

scores = cross_val_score(
    pipeline,
    X,y,
    cv=5,
    scoring="accuracy"   
)

average_accuracy = scores.mean()

print("Average Accuracy: ", average_accuracy)

plt.bar(
    ["Pipeline"],
    [average_accuracy]
)
plt.title("Pipeline Accuracy")
plt.ylabel("Accuracy")
plt.show()