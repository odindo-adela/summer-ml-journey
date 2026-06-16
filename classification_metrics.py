import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import(
    accuracy_score, 
    confusion_matrix,
    classification_report
    )

df = pd.read_csv("soccer_positions.csv")

df["Position"] = df["Position"].map({
    "Forward":1,
    "Winger":2
})

df["Elite Player"] = (df["Goals"] > 20).astype(int)

X = df[["Matches", "Assists", "Position"]]
y = df["Elite Player"]

X_train, X_test, y_train, y_test = train_test_split(
    X,y,
    test_size=0.3,
    random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print("\nPredictions: ", predictions)
print("\nActual Values: ", y_test.values)

accuracy = accuracy_score(y_test, predictions)
print("\nAccuracy: ", accuracy)

cm = confusion_matrix(y_test, predictions)
print("\nConfusion Matrix: ")
print(cm)

report = classification_report(y_test, predictions)
print("\nClassification Report: ")
print(report)

probabilities = model.predict_proba(X_test)
print("\nProbability: ")
print(probabilities)
