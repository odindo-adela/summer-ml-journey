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
    num1 = float(input("Enter first number: "))
    operator = input("Choose your operation(+,-,/,*): ")
    num2 = float(input("Enter second number: "))
    result = calculator(num1, operator,num2)
    print(result)

    again=input("Do you want to continue?(yes/no): ")
    if again.lower() == "no":
        break