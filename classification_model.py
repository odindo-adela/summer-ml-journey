import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score 
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

df = pd.read_csv("soccer_player.csv")

df["Elite Player"] = df["Goals"] > 20

X = df[["Matches", "Assists"]]
y = df["Elite Player"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print("Predictions: ", predictions)
print("Actual Category: ", y_test.values)

accuracy = accuracy_score(y_test, predictions)
print("Accuracy: ", accuracy)

probability = model.predict_proba(X_test)
print("Probability: ", probability)

cm = confusion_matrix(y_test, predictions)
print("Confusion Matrix: \n", cm)

print(classification_report(y_test, predictions))