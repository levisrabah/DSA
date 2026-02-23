# Division
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if num2 != 0: # Check for division by zero
    result = num1 / num2
    print(f"Division: {num1} / {num2} = {result}")
else:
    print("Error: Division by zero is not allowed.")