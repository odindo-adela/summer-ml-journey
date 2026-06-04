import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error 
import matplotlib.pyplot as plt
df = pd.read_csv("soccer_positions.csv")

df["Position"] = df["Position"].map({
    "Forward": 1,
    "Winger": 2
})

y = df["Goals"]

def evaluate_model(features, seed):
    X = df[features]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=seed)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    error = mean_absolute_error(y_test, predictions)
    return error

seed_0 = evaluate_model(["Matches", "Assists", "Position"], 0)
seed_1 = evaluate_model(["Matches", "Assists", "Position"], 1)
seed_2 = evaluate_model(["Matches", "Assists", "Position"], 2)
seed_3 = evaluate_model(["Matches", "Assists", "Position"], 3)
seed_4 = evaluate_model(["Matches", "Assists", "Position"], 4)
seed_5 = evaluate_model(["Matches", "Assists", "Position"], 5)

print("Seed 0: ", seed_0)
print("Seed 1: ", seed_1)
print("Seed 2: ", seed_2)
print("Seed 3: ", seed_3)
print("Seed 4: ", seed_4)

maes = []
 
for seed in [0, 1, 2, 3, 4, 5]:
    mae = evaluate_model(["Matches", "Assists", "Position"], seed)
    maes.append(mae)

print(maes)

average_mae = sum(maes) / len(maes)
print("Average MAE: ", average_mae)

lowest_mae = min(maes)
highest_mae = max(maes)

print("Lowest MAE: ", lowest_mae)
print("Highest MAE: ", highest_mae)

seeds = [0,1,2,3,4,5]
plt.plot(seeds, maes)
plt.title("Model Perfomance Across Different Train/Test Splits")
plt.xlabel("Random State")
plt.ylabel("MAE")
plt.show