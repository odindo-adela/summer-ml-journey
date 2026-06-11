import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df = pd.read_csv("soccer_positions.csv")
df["Position"] = df["Position"].map({
    "Forward": 1,
    "Winger": 2,
    })

def evaluate_model(features):
    X = df[features]
    y = df["Goals"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    prediction_train = model.predict(X_train)
    prediction_test = model.predict(X_test)

    train_mae = mean_absolute_error(y_train, prediction_train)
    test_mae = mean_absolute_error(y_test, prediction_test)

    return train_mae, test_mae

# Model A
mae_a = evaluate_model(["Matches"])
# Model B
mae_b = evaluate_model(["Matches","Position"])
# Model C
mae_c = evaluate_model(["Matches","Position","Assists"])

print("Model A")
print("Training MAE: ", mae_a[0])
print("Testing MAE: ", mae_a[1])

print("\nModel B")
print("Training MAE: ", mae_b[0])
print("Testing MAE: ", mae_b[1])

print("\nModel C")
print("Training MAE: ", mae_c[0])
print("Testing MAE: ", mae_c[1])

plt.bar(
    ["Train", "Test"],
    [mae_a[0], mae_a[1]]
)
plt.title("Model A Error")
plt.ylabel("MAE")
plt.show()

plt.bar(
    ["Train", "Test"],
    [mae_b[0], mae_b[1]]
)
plt.title("Model B Error")
plt.ylabel("MAE")
plt.show()

plt.bar(
    ["Train", "Test"],
    [mae_c[0], mae_c[1]]
)
plt.title("Model C Error")
plt.ylabel("MAE")
plt.show()