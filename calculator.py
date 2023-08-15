Can you read a README GITHUB file in Markdown for the code:

import math

# Welcome message
print("Welcome to the Advanced Calculator!")

# Initialize memory for storing values
memory = 0

# Main loop for user interaction
while True:
    # Input: Get the first number from the user
    num1 = float(input("Enter the first number: "))
    
    # Input: Get the operation from the user
    operation = input("Enter the operation (+, -, *, /, **, sqrt, %, sin, cos, tan, M+, M-, MR, MC, q to quit): ")
    
    # Check if the user wants to quit the calculator
    if operation == "q":
        print("Goodbye!")
        break  # Exit the loop and terminate the program
    
    # For operations that require a second number, get the second number from the user
    if operation not in ["sqrt", "sin", "cos", "tan", "M+", "M-", "MR", "MC"]:
        num2 = float(input("Enter the second number: "))
    
    # Perform the selected operation based on user input
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            continue  # Skip the rest of the loop and go back to the start
    elif operation == "**":
        result = num1 ** num2
    elif operation == "sqrt":
        if num1 >= 0:
            result = math.sqrt(num1)
        else:
            print("Error: Cannot calculate square root of a negative number.")
            continue  # Skip the rest of the loop and go back to the start
    elif operation == "%":
        result = num1 % num2
    elif operation == "sin":
        result = math.sin(num1)
    elif operation == "cos":
        result = math.cos(num1)
    elif operation == "tan":
        result = math.tan(num1)
    elif operation == "M+":
        memory += num1
    elif operation == "M-":
        memory -= num1
    elif operation == "MR":
        result = memory
    elif operation == "MC":
        memory = 0
    else:
        print("Error: Invalid operation entered.")
        continue  # Skip the rest of the loop and go back to the start
    
    # Display the result of the operation, rounded to 2 decimal places
    print("Result:", round(result, 2))
    
    # Ask the user if they want to perform another calculation
    another_calculation = input("Thank you! Do you want to perform another calculation? (yes/no): ")
    if another_calculation.lower() != "yes":
        print("Goodbye!")
        break  # Exit the loop and terminate the program
