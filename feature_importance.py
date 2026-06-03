import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("soccer_positions.csv")

df["Position"] = df["Position"].map({
    "Forward": 1,
    "Winger": 2
})

X = df[["Matches", "Assists", "Position"]]
y = df["Goals"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

print("Intercept: ", model.intercept_)

print("\nCoefficients: ")
for feature, coefficient in zip(X.columns, model.coef_):
    print(f"{feature}: {coefficient}")

print("\nCorrelation: ")
print(df.corr(numeric_only=True))