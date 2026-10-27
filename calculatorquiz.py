num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Choose an operation to continue:")
print("1. Addition")
print("2. Subtraction")
print("3.Multiplication")
print("4. Division")

operation = input("Enter the operation you are continuing with: ")

if operation == '1':
    result = num1 + num2
    print(f"{result} = {num1} + {num2}")
elif operation == '2':
    result = num1 - num2
    print(f"{result} = {num1} - {num2}")
elif operation == '3':
    result = num1 * num2
    print(f"{result} = {num1} * {num2}")
elif operation == '4':
    if num2 != '0':
        result = num1 / num2
        print(f"{result} = {num1} / {num2}")
    else:
        print("Error: Division by zero is not allowed")
else:
    print("Invalid choice of operation.")