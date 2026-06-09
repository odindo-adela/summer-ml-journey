import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("soccer_positions.csv")

df["Position"] = df["Position"].map({
    "Forward":1,
    "Winger":2
})


print("Data Set First Five Rows:")
print(df.head())

print("\nSet Data Types:")
print(df.info())

print("\nDataset Statistics:")
print(df.describe())

print(df["Position"].value_counts())

print("Player with Most Goals")
print(df.loc[df["Goals"].idxmax()])

print("\nPlayer with Least Goals")
print(df.loc[df["Goals"].idxmin()])

print("\nPlayer with Most Assists")
print(df.loc[df["Assists"].idxmax()])

print("\nPlayer with Least Assists")
print(df.loc[df["Assists"].idxmin()])

plt.hist(df["Goals"])
plt.title("Goals Distribution")
plt.xlabel("Goals")
plt.ylabel("Number of Players")
plt.show()

plt.hist(df["Assists"])
plt.title("Assists Distribution")
plt.xlabel("Assists")
plt.ylabel("Number of Players")
plt.show()

df["Position"].value_counts().plot(kind="bar")
plt.title("Position Counts")
plt.xlabel("Positions")
plt.ylabel("Number of Players")
plt.show()

correlation = df.corr(numeric_only=True)
plt.imshow(correlation)
plt.colorbar()

plt.xticks(
    range(len(correlation.columns)),
    correlation.columns,
    rotation=45
)
plt.yticks(
    range(len(correlation.columns)),
    correlation.columns
)

plt.title("Correlation Heatmap")
plt.show()
