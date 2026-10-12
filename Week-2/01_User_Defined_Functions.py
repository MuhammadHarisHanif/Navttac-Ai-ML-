

# NAVTTC AI/ML - Week 2
# Task 20: User-Defined Functions

# Example 1: Simple function
def greet():
    print("Hello! Welcome to Python.")

greet()


# Example 2: Function with parameters
def greet_user(name):
    print("Hello,", name)

greet_user("Ali")


# Example 3: Function to add two numbers
def add_numbers(a, b):
    return a + b

result = add_numbers(10, 20)
print("Sum =", result)


# Example 4: Function to calculate square
def square(number):
    return number * number

print("Square =", square(5))


# Example 5: Function with a default parameter
def welcome(name="Student"):
    print("Welcome,", name)

welcome()
welcome("Ahmed")


# Example 6: Function to check even or odd
def check_even_odd(number):
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")

check_even_odd(8)
check_even_odd(7)
