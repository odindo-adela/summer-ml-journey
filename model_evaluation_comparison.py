import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import(
    train_test_split,
    cross_val_score)
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv("soccer_positions.csv")

df["Position"] = df["Position"].map({
    "Forward":1,
    "Winger":2
})

df["Elite Player"] = (df["Goals"]>25).astype(int)

X = df[["Matches", "Assists", "Position"]]
y = df["Elite Player"]

X_train, X_test, y_train, y_test = train_test_split(
    X,y,
    test_size=0.3,
    random_state=42
)

model = LogisticRegression()
model.fit(X_train,y_train)

split_predictions = model.predict(X_test)

split_accuracy = accuracy_score(y_test, split_predictions)
print("\nSplit Accuracy: ", split_accuracy)

cv_scores = cross_val_score(
    model,
    X,y,
    cv=5,
    scoring="accuracy"
)

cv_accuracy = cv_scores.mean()
print("\nCross Validation Accuracy: ", cv_accuracy)

plt.bar(
    ["Train/Test Split", "Cross Validation"],
    [split_accuracy, cv_accuracy]
)
plt.title("Accuracy Comparison")
plt.ylabel("Accuracy")
plt.show()

difference = abs(split_accuracy - cv_accuracy)
print("\nDifference: ", difference)