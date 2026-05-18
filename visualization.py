import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("soccer_player.csv")

plt.plot(df["Name"], df["Assists"])

plt.title("Player Assists")
plt.xlabel("Players")
plt.ylabel("Assists")

plt.show()

top_players = df[df["Goals"]>25]
plt.plot(top_players["Name"], top_players["Goals"])

plt.title("Top Goal Scorers")
plt.xlabel("Players")
plt.ylabel("Goals")

plt.show()
