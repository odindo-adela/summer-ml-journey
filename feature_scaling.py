import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error


df = pd.read_csv("soccer_positions.csv")

df["Position"] = df["Position"].map({
    "Forward":1,
    "Winger":2
})

df["Salary"] = [
    500000,
    750000,
    1200000,
    2000000,
    3000000,
    4500000,
    6000000,
    8000000,
    9500000,
    550000
]

print(df.describe())

X = df[["Matches", "Assists", "Position", "Salary"]]
y = df["Goals"]

print(X.head())

# Model A
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model_a = LinearRegression()
model_a.fit(X_train, y_train)
predictions_1 = model_a.predict(X_test)

error_1 = mean_absolute_error(y_test, predictions_1)
print("Error without sclaing:", error_1)

# Model B
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print(X_scaled[:5])

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.3, random_state=42
)

model_b = LinearRegression()
model_b.fit(X_train, y_train)
predictions_2 = model_b.predict(X_test)

error_2 = mean_absolute_error(y_test, predictions_2)
print("Error with sclaing:", error_2)
