import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv("soccer_player.csv")

X = df[["Matches"]]
y = df["Goals"]

model = LinearRegression()
model.fit(X, y)

predictions = model.predict(X)

plt.scatter(df["Matches"], df["Goals"])
plt.plot(df["Matches"], predictions)

plt.xlabel("Matches")
plt.ylabel("Goals")
plt.title("Regression Model: Matches vs Goals")

plt.show()

df["Predicted_Goals"] = predictions
df["Residual"] = df["Goals"] - df["Predicted_Goals"]
print(df)

plt.scatter(df["Matches"], df["Residual"])
plt.axhline(y=0)
plt.title("Residuals Plot")
plt.xlabel("Matches")
plt.ylabel("Residuals")
plt.show()
