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

