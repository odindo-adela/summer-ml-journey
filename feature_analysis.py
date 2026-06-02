import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("soccer_player.csv")
print(df.describe())

print(df.corr(numeric_only=True))

plt.scatter(df["Matches"], df["Goals"])
plt.title("Matches vs Goals")
plt.xlabel("Matches")
plt.ylabel("Goals")
plt.show()

plt.scatter(df["Assists"], df["Goals"])
plt.title("Assists vs Goals")
plt.xlabel("Assists")
plt.ylabel("Goals")
plt.show()