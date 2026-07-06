import pandas as pd
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

df = pd.read_csv("soccer_positions.csv")

df["Position"] = df["Position"].map({
    "Forward":1,
    "Winger":2
})

df["Elite Player"] = (df["Goals"]>25).astype(int)

df["Goal Contribution"] = df["Goals"]+df["Assists"]

print(df)

# Model A
X = df[["Matches", "Assists", "Position", "Goal Contribution"]]
y = df["Elite Player"]

model = RandomForestClassifier(random_state=42)

model_accuracy = cross_val_score(
    model,
    X,y,
    cv=5,
    scoring="accuracy"
).mean()

print("Accuracy: ", model_accuracy)

# Model B
X = df[["Matches", "Assists", "Position"]]
y = df["Elite Player"]

model_accuracy_2 = cross_val_score(
    model,
    X,y,
    cv=5,
    scoring="accuracy"
).mean()

print("Accuracy 2: ", model_accuracy_2)

plt.bar(
    ["Original Features", "Engineered Features"],
    [model_accuracy_2, model_accuracy]
)
plt.ylabel("Accuracy")
plt.title("Original vs Engineered Features Accuracy")
plt.show()