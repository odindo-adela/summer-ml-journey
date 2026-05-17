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