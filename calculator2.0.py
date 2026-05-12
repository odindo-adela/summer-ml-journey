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
            return "Can not perform zero division!"
        else:
            result=num1/num2

    else:
        return "Invalid operator!"

    return result

while True:
    print("\nCalculation Menu:")
    print("Option 1. Calculate")
    print("Option 2. View History")
    print("Option 3. Exit")
    choice= input("Choose an option(1, 2 or 3):")

    if choice=="1":
        num1 = float(input("Enter first number: "))
        operator = input("Choose your operation(+,-,/,*): ")
        num2 = float(input("Enter second number: "))
        result = calculator(num1, operator,num2)
        
        if isinstance(result, (int,float)):
            with open("history.txt", "a") as file:
                file.write(f"{num1} {operator} {num2} = {result}\n")

            
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