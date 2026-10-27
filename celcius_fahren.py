print("Select a conversion.")
print("1. Celcius to Fahrenheit.")
print("2. Fahrenheit to Celcius.")

option = input("Enter your option: ")

if option == '1':
    celcius_input = float(input("Enter temperature in celcius: "))
    fahrenheit = (celcius_input * 9/5) + 32
    print(f"The temperature in Celcius converted is equal to {fahrenheit} F")

elif option == '2':
    fahrenheit_input = float(input("Enter temperature in fahrenheit: "))
    celcius = (fahrenheit_input - 32) * 5/9
    print(f"The temperature in fahrenheit converted id equal to {celcius} C")

else:
    print("Please select the appropriate option.")
