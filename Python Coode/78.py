# Wap to demonstrate different types of parameters

# Positional Parameters
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")
    
greet("Alice", 30)
print("This is the result for Positional Parameters.\n")


# Default Parameters
def greet(name, age=25):
    print(f"Hello, {name}! You are {age} years old.")
    
greet("Alice")
print("This is the result of Default Parameters.\n")


# Keyword Parameters
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")
    
greet(name="Alice", age=30)
print("This is the result of Keyword Parameters.")

# Variable-length Parameters

# Using *args for variable number of arguments (positional arguments)
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3))
print(sum_numbers(4, 5, 6, 7, 8))
print("This is the result for *args (variable-length positional parameters).\n")


# Using **kwargs for variable number of keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")
print("This is the result for **kwargs (variable-length keyword parameters).")

print("THIS PROGRAM IS WRITTEN BY Monish :- 0221BCA156")