# A simple, user-friendly calculator program

def calculator():
    print("Welcome to the Simple Calculator!")

    try:
        # Prompt the user to enter the first number
        num1 = float(input("Enter the first number: "))

        # Prompt the user to enter the second number
        num2 = float(input("Enter the second number: "))

        # Show available operations
        print("\nWhich operation would you like to perform?")
        print("Type + for Addition")
        print("Type - for Subtraction")
        print("Type * for Multiplication")
        print("Type / for Division")

        # Get the user's operation choice
        operation = input("Enter your choice: ")

        # Perform the selected operation
        if operation == '+':
            result = num1 + num2
            print(f"\nResult: {num1} + {num2} = {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"\nResult: {num1} - {num2} = {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"\nResult: {num1} * {num2} = {result}")
        elif operation == '/':
            if num2 == 0:
                print("\nError: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"\nResult: {num1} / {num2} = {result}")
        else:
            print("\nInvalid operation. Please choose from +, -, *, or /.")

    except ValueError:
        print("\nInvalid input. Please enter numeric values only.")

# Run the calculator function
calculator()