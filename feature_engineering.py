import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error


df = pd.read_csv("soccer_player.csv")

df["Goals_Per_Match"] = df["Goals"] / df["Matches"]

df["Goals_Assist_Total"] = df["Goals"] + df["Assists"]

df["Assists_Per_Match"] = df["Assists"] / df["Matches"]

print(df)

print(df.corr(numeric_only=True))

# Model A
X = df[["Matches"]]
y = df["Goals"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model_1 = LinearRegression()
model_1.fit(X_train, y_train)

predictions_1 = model_1.predict(X_test)
error_1 = mean_absolute_error(y_test, predictions_1)
print("MAE_1: ", error_1)

# Model B
X = df[["Matches", "Assists"]]
y = df["Goals"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model_2 = LinearRegression()
model_2.fit(X_train, y_train)

predictions_2 = model_2.predict(X_test)
error_2 = mean_absolute_error(y_test, predictions_2)
print("MAE_2: ", error_2)

# Model C
X = df[["Matches", "Goals_Assist_Total"]]
y = df["Goals"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model_3 = LinearRegression()
model_3.fit(X_train, y_train)

predictions_3 = model_3.predict(X_test)
error_3 = mean_absolute_error(y_test, predictions_3)
print("MAE_3: ", error_3)