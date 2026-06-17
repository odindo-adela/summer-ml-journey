import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score


# Loading data
df = pd.read_csv("soccer_positions.csv")

# Encoding Position
df["Position"] = df["Position"].map({
    "Forward":1,
    "Winger":2
})

# Elite Player
df["Elite Player"] = (df["Goals"] > 25).astype(int)
print(df)

# Target + Features
X = df[["Matches", "Assists", "Position"]]
y = df["Elite Player"]

# Logistic Regression Model
model_a = LogisticRegression()
score_a = cross_val_score(
    model_a,
    X,y,
    cv=5,
    scoring="accuracy"
)
print("\nLogistic Regression Accuracy: ")
print(score_a.mean())

# Decision Tree Model
model_b = DecisionTreeClassifier(max_depth=3)
score_b = cross_val_score(
    model_b,
    X,y,
    cv=5,
    scoring="accuracy"
)
print("\nDecision Tree Accuarcy: ")
print(score_b.mean())

# Determining which model has a higher accuracy
if score_b.mean() > score_a.mean():
    print("\nLDecision Tree Model Wins!")
else:
    print("\nLogistic Regression Model Wins!")

# Visualization
plt.bar(
    ["Logistic Regression", "Decision Tree"],
    [score_a.mean(), score_b.mean()]
    )
plt.title("Model Accuracy")
plt.ylabel("Accuracy Score")
plt.show()