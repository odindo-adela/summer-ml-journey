import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error 

df = pd.read_csv("soccer_positions.csv")

df["Position"] = df["Position"].map({
    "Forward": 1,
    "Winger": 2
})

y = df["Goals"]

def evaluate_model(features):
    X = df[features]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    error = mean_absolute_error(y_test, predictions)
    return error

mae_a = evaluate_model(["Matches"])
mae_b = evaluate_model(["Matches", "Assists"])
mae_c = evaluate_model(["Matches", "Assists", "Position"])

print("Model A(Matches): ", mae_a)
print("Model B(Matches + Assists): ", mae_b)
print("Model C(Matches + Assists + Position): ", mae_c)

if mae_a<mae_b and mae_a<mae_c:
    print("Best Model: Model A")
elif mae_b<mae_a and mae_b<mae_c:
    print("Best Model: Model B")
else:
    print("Best Model: Model C")
