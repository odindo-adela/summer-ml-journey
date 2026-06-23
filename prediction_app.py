import joblib

model = joblib.load("elite_player_model.pkl")

matches = int(input("Enter matches: "))
assists = int(input("Enter assists: "))
position = input("Enter Position (Forward/Winger): ")

if position == "Forward":
    position = 1
else:
    position = 2

prediction = model.predict(
    [[matches,assists,position]]
)

probabilities = model.predict_proba(
    [[matches, assists, position]]
)

if prediction[0] == 1:
    confidence = probabilities[0][1]
    print("\nElite Player")
else:
    confidence = probabilities[0][0]
    print("\nNot Elite Player")

print(
    "Confidence: ",
    round(confidence*100,2),
    "%"
)