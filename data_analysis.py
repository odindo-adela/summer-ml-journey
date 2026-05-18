import pandas as pd

df = pd.read_csv("soccer_player.csv")
print(df)

print(df.head())

print(df.columns)

print(df["Goals"])

print(df["Goals"].mean())

print(df["Goals"].max())

print(df[df["Goals"]>25])