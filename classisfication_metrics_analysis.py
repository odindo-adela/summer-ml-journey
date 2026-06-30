import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score, confusion_matrix, precision_score, recall_score, f1_score)

df = pd.read_csv("soccer_positions.csv")

df["Position"] = df["Position"].map({
    "Forward":1,
    "Winger":2
})

df["Elite Player"] = (df["Goals"]>25).astype(int)

X = df[["Matches", "Assists", "Position"]]
y = df["Elite Player"]

model = RandomForestClassifier()

X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=42, test_size=0.3)

model.fit(X_train, y_train)

prediction = model.predict(X_test)

accuracy = accuracy_score(y_test,prediction)
print("Accuracy: ", accuracy)

cm = confusion_matrix(y_test, prediction)
print("\nConfusion Matrix: ", cm)

precision = precision_score(y_test,prediction)
print("\nPrecision Score: ", precision)

recall = recall_score(y_test,prediction)
print("\nRecall Score: ", recall)

f1 = f1_score(y_test,prediction)
print("\nF1 Score: ", f1)