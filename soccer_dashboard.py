import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("soccer_player.csv")

top_scorers = df[df["Goals"]>25]

def display_menu():
    print("\nSelect your option:")
    print("Option 1. View Dataset")
    print("Option 2. View Top Scorers")
    print("Option 3. Show Average Goals")
    print("Option 4. Visualize Goals")
    print("Option 5. Search Player")
    print("Option 6. Exit")
    

while True:
    display_menu()
        
    choice = input("Choose an option(1, 2, 3, 4, 5 or 6): ")

    if choice == "1":
        print(df)

    elif choice == "2":
        print("/nTop Scorers:", top_scorers)

    elif choice == "3":
        average = df["Goals"].mean()
        print("\nAverage Goals: ", average)

    elif choice == "4":
        plt.bar(top_scorers["Name"], top_scorers["Goals"])

        plt.title("Top Scorers")
        plt.xlabel("Players")
        plt.ylabel("Number of Goals")

        plt.show()

    elif choice == "5":
        player_name = input("Enter player name: ")
        
        search = df[df["Name"]==player_name]
        if search.empty:
            print("\nPlayer not found!")
        else:
            print("/nPlayer Found: ")
            print(search)
    
    elif choice == "6":
        print("\nExiting, thank you!")
        break

    else:
        print("\nInvalid option! Kindly select(1, 2, 3, 4, 5 or 6)")