import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error

df = pd.read_csv("soccer_player.csv")

X = df[["Matches"]]
y = df["Goals"]

X_train, X_test, y_train, y_test = train_test_split( X, y, random_state=42, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

train_predictions = model.predict(X_train)
test_predictions = model.predict(X_test)

plt.scatter(X_train,y_train, label="Training Data")
plt.scatter(X_test, y_test, label="Testing Data")
plt.plot(X_train, train_predictions, label="Regression Line")
plt.title("Linear Regression: Matches vs Goals")
plt.xlabel("Matches Played")
plt.ylabel("Goals Scored")

plt.legend()
plt.show()

training_error = mean_absolute_error(y_train, train_predictions)
print("Training Error: ", training_error)

testing_error = mean_absolute_error(y_test, test_predictions)
print("Testing Error: ", testing_error)