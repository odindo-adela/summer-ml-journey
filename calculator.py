num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))

operation = input("Enter operation:")
result = None

if operation == "+":
    result = num1+num2

elif operation == "-":
    result = num1-num2

elif operation == "*":
    result = num1*num2

elif operation == "/":
    if num2==0:
        print("Can not divide by zero")
    else:
        result = num1/num2

else:
    print("Invalid!Enter either: +, -, /, *")

if result is not None:
    print(f"Final results:{result}")