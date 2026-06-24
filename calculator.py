
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

print("Calculator APP")
while True:
    operation = input("Please select an operation: ")
    num1 = int(input("Enter first value: "))
    num2 = int(input("Enter second value: "))

    if operation == "add":
        print(add(num1, num2))
    elif operation == "subtract":
        print(subtract(num1, num2))
    elif operation == "multiply":
        print(multiply(num1, num2))
    elif operation == "divide":
        print(divide(num1, num2))
    else:
        print("Incorrect input")

    again = input("Would you like to calculate something else? 'y' or 'n'")
    if again == 'y':
        pass
    else:
        break




