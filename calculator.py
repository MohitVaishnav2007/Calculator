num1 = int(input("Enter your first number: ", ))
operation = input("Enter the operation (+, -, *, /): ", )
num2 = int(input("Enter your second number: ", ))

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
        result = "Error: Division by zero is not allowed."
else:
    result = "Error: Invalid operation."

print(result)
