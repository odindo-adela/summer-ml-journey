import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

df = pd.read_csv("soccer_player.csv")

X = df[["Matches", "Assists"]]
y = df[["Goals"]]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Predictions:", predictions)
print("Actaul Values:", y_test.values)

error = mean_absolute_error(y_test, predictions)
print("Mean Absolute Error:", error)