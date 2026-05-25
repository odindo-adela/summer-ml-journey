import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

df = pd.read_csv("messy_soccer_data.csv")

print(df)
print(df.isnull())
print(df.isnull().sum())

df["Goals"] = df["Goals"].fillna(df["Goals"].mean())
print(df)

df["Assists"] = df["Assists"].fillna(df["Assists"].mean())
print(df)

df["Matches"] = df["Matches"].fillna(df["Matches"].mean())
print(df)

df["Position"] = df["Position"].map({
    "Forward": 1,
    "Winger": 2
})
print(df)

df["Goals_Per_Match"] = df["Goals"] / df["Matches"]
print(df)

X = df[["Assists", "Matches", "Position", "Goals_Per_Match"]]
y = df["Goals"]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

prediction = model.predict(X_test)
print("Predictions: ", prediction )
print("Actual Values:", y_test.values)

error = mean_absolute_error(y_test, prediction)
print("Mean Absolute Error: ", error)

plt.scatter(df["Goals_Per_Match"], df["Goals"])
plt.show()