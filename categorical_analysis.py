import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

df = pd.read_csv("soccer_positions.csv")

df["Position"] = df["Position"].map({
    "Forward": 1,
    "Winger": 2
})

# Model A
X = df[["Matches", "Assists", "Position"]]
y = df["Goals"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model_1 = LinearRegression()
model_1.fit(X_train, y_train)

predictions_1 = model_1.predict(X_test)
print("Predictions_1: ", predictions_1)

error_1 = mean_absolute_error(y_test, predictions_1)
print("MAE_1: ", error_1)

# Model B
X = df[["Matches", "Assists"]]
y = df["Goals"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model_2 = LinearRegression()
model_2.fit(X_train, y_train)

predictions_2 = model_2.predict(X_test)
print("Predictions_2: ", predictions_2)

error_2 = mean_absolute_error(y_test, predictions_2)
print("MAE_2: ", error_2)