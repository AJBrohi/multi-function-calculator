import math, os

def add (n1, n2):
    return n1 + n2

def subtract (n1, n2):
    return n1 - n2

def multiply (n1, n2):
    return n1 * n2

def division (n1, n2):
    return n1 / n2

def exponent(n1, n2):
    return n1 ** n2

def logarithm(n1):
    return math.log(n1)

def square_root(n1):
    return math.sqrt(n1)

def calculator():
    clear()
    num1 = float(input("Enter First Number: "))

    should_run = True

    while should_run:
        for key in operations:
            print(key, end=" ")

        chosen_symbol=input("\nChoose an operation from the symbols: ")

        if chosen_symbol not in operations:
            print("You've chosen a wrong operations. Please Try Again!")
            break

        operation_function = operations[chosen_symbol]

        if chosen_symbol in ["log", "sqrt"]:
            answer = round(operation_function(n1=num1),2)
            print(f"{chosen_symbol} of {num1} is {(answer)}")
        else:
            num2 = float(input("Enter Next Number: "))
            answer = round(operation_function(n1=num1, n2=num2),2)

            print(f"{num1} {chosen_symbol} {num2} = {answer}")

        user_choice = input("Type 'Y' to continue calculation with the current answer or 'N' to exit or type anything to reset the values - ").lower()
        
        if user_choice == 'y':
            num1 = answer
            print(f"Current Answer: {answer}")
        elif user_choice == 'n':
            should_run = False
        else:
            should_run = False
            calculator()            

clear = lambda: os.system('cls')

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division,
    "exp": exponent,
    "log": logarithm,
    "sqrt": square_root
}

calculator()