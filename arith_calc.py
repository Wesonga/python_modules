num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Select the operation to use.")

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

operation = input("Select operation: ")

if operation == '1':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == '2':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == '3':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == '4':
    if num2 != '0':
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("The second number must not be zero")
else:
    print("Invalid operation selected")
