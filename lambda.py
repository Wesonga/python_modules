def get_greeting():
    return "Hello"

greet_var = get_greeting
print(greet_var)

#  lambda functions - a quick throw away function with no name

def double(x):
    return x * 2

# lamda version

double1 = lambda x: x * 2
add = lambda a, b: a + b 

print(double1(4))
print(add(2, 4))

