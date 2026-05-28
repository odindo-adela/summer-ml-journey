import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

df = pd.read_csv("soccer_player.csv")

X = df[["Matches", "Assists"]]
y = df["Goals"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

print("Model Coefficient: ", model.coef_)
print("Model Intercept: ", model.intercept_)

predictions = model.predict(X_test)
print("Prediction: ", predictions)
print("Actual Value: ", y_test.values)

error = mean_absolute_error(y_test, predictions)
print("MAE: ", error)

plt.scatter(y_test, predictions)
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Actual vs Predicted Values")
plt.show()

residual = y_test - predictions

plt.scatter(predictions, residual)
plt.axhline(y=0)
plt.xlabel("Predicted Goals")
plt.ylabel("Residual")
plt.title("Residuals Plot")
plt.show()