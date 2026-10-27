# function that adds three numbers
def addition(a, b, c):
    return a + b + c

result = addition(1, 3, 5)
print(result)



# function that checks if a number is even
def even(number):
    if number % 2 ==0:
        print(f"The number {number} is even")
        
even_number = int(input("Enter a number to check if even: "))

if_even = even(even_number)
print(if_even)



# function that takes two strings and prints them combined (string concatination)
def sum_string(str1, str2):
    print(f"{str1} {str2}")
    
sum_string("Hello", "world!")

