# syntax: when you do not follow python rules

# runtime: code structure is fine but sth goes wrong during running the program

try:
    # code that might cause an error
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"The result is {result}")
except ZeroDivisionError:
    print("You can not divide by zero.")

except ValueError:
    print("Please enter a valid number.")
    
 # code that runs if there is an error
except Exception:
    print("Oops! Something went wrong!")
    
# debugging
def divide (a, b):
    print(f"Dividing {a} by {b}")
    return a / b

divide(2, 5)

# tracebacks


    
