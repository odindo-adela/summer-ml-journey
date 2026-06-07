import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df = pd.read_csv("soccer_positions.csv")

df["Position"] = df["Position"].map({
    "Forward": 1,
    "Winger": 2
})

df["Goals_Doubled"] = df["Goals"] * 2

y = df["Goals"]


def evaluate_model(features):
    X = df[features]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    train_predictions = model.predict(X_train)
    test_predictions = model.predict(X_test)

    training_error = mean_absolute_error(y_train, train_predictions)
    testing_error = mean_absolute_error(y_test, test_predictions)

    return training_error, testing_error


mae_a = evaluate_model(["Matches"])
mae_b = evaluate_model(["Matches", "Assists", "Position"])
mae_c = evaluate_model(["Matches", "Assists", "Position", "Goals_Doubled"])

print("Model A")
print("Training_MAE:",mae_a[0])
print("Testing_MAE:",mae_a[1])

print("Model B")
print("Training_MAE:",mae_b[0])
print("Testing_MAE:",mae_b[1])

print("Model C")
print("Training_MAE:",mae_c[0])
print("Testing_MAE:",mae_c[1])

plt.bar(
    ["Training", "Testing"],
    [mae_a[0], mae_a[1]]
)
plt.title("Model A Error")
plt.ylabel("MAE")
plt.show()

plt.bar(
    ["Training", "Testing"],
    [mae_b[0], mae_b[1]]
)
plt.title("Model B Error")
plt.ylabel("MAE")
plt.show()

plt.bar(
    ["Training", "Testing"],
    [mae_c[0], mae_c[1]]
)
plt.title("Model C Error")
plt.ylabel("MAE")
plt.show()