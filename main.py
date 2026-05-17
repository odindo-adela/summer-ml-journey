from calculator import calculator

from utils import display_menu, get_number
operations = {
    "+":"Addition",
    "-":"Subtraction",
    "/":"Division",
    "*":"Multiplication"
}

history_list=[]

while True:
    display_menu()
    
    choice = input("Choose an option(1, 2, or 3): ")
    
    if choice=="1":
        num1 = get_number("Enter first number: ")
        
        operator = input ("Choose your operation(+, -, *, /): ")
        
        num2 = get_number("Enter second number: ")
        
        result = calculator(num1, operator, num2)
        
        if isinstance(result, (int, float)):
            with open("history.txt", "a") as file:
                file.write(f"{num1} {operator} {num2} = {result}\n")

            history_list.append(f"{num1} {operator} {num2} = {result}")

        print("Result:", result)
        
    elif choice=="2":
        with open("history.txt", "r") as file:
            history = file.read()

            if history.strip():
                print("Calculation History:")
                print(history)

            else:
                print("History is empty")
                

    elif choice=="3":
        print("Exiting Calculator, Thank you!")
        break

    else:
        print("Invalid choice! Kindly select 1, 2 or 3")
