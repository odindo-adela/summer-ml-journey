import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df = pd.read_csv("soccer_positions.csv")
df["Position"] = df["Position"].map({
    "Forward": 1,
    "Winger": 2,
    })

y = df["Goals"]

def evaluate_model(features):
    X = df[features]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    error = mean_absolute_error(y_test, predictions)
    return error

# Model A
mae_a = evaluate_model(["Matches"])
print("Model A MAE: ", mae_a)

# Model B
mae_b = evaluate_model(["Assists"])
print("\nModel B MAE: ", mae_b)

# Model C
mae_c = evaluate_model(["Position"])
print("\nModel C MAE: ", mae_c)

# Model D
mae_d = evaluate_model(["Matches","Assists"])
print("\nModel D MAE: ", mae_d)

# Model E
mae_e = evaluate_model(["Matches","Position"])
print("\nModel E MAE: ", mae_e)

# Model F
mae_f = evaluate_model(["Matches","Assists","Position"])
print("\nModel F MAE: ", mae_f)

results = {
    "A": mae_a,
    "B": mae_b,
    "C": mae_c,
    "D": mae_d,
    "E": mae_e,
    "F": mae_f
}

best_model = min(results, key=results.get)
print("\nBest Model: ", best_model)
print("Lowest MAE: ", results[best_model])

plt.bar(
    results.keys(),
    results.values()
)
plt.title("Model MAE Comparison")
plt.xlabel("Models")
plt.ylabel('MAE')
plt.show()