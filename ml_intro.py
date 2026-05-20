import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("soccer_player.csv")

X = df[["Matches"]]
y = df["Goals"]

model = LinearRegression()
model.fit(X,y)

prediction = model.predict([[40]])

print(prediction)

import matplotlib.pyplot as plt

plt.scatter(df["Matches"], df["Goals"])
plt.xlabel("Matches")
plt.ylabel("Goals")
plt.title("Matches vs Goals")

plt.show()