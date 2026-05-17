def calculator(num1,operator,num2):
    result = None
    
    if operator=="+":
        result=num1+num2
        
    elif operator=="-":
        result=num1-num2
        
    elif operator=="*":
        result=num1*num2
        
    elif operator=="/":
        if num2==0:
            return "Cannot perform zero division!"
        else:
            result=num1/num2

    else:
        return "Invalid operator!"

    return result

operations = {
    "+":"Addition",
    "-":"Subtraction",
    "/":"Division",
    "*":"Multiplication"
}

history_list=[]

def display_menu():
    print("\nCalculation Menu:")
    print("Option 1. Calculate")
    print("Option 2. View History")
    print("Option 3. Exit")
    
def get_number(message):
    while True:
        try:
             number = float(input(message))
             return number
        
        except ValueError:
            print("Invalid! Please enter a number.")

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
