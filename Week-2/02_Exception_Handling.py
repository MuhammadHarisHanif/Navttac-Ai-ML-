

# NAVTTC AI/ML - Week 2
# Task 26: Exception Handling

# Example 1: Handle division by zero
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print("Result =", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid numbers.")

finally:
    print("Program finished.")


# Example 2: Handle invalid list index
numbers = [10, 20, 30]

try:
    index = int(input("Enter a list index (0-2): "))
    print("Value =", numbers[index])

except IndexError:
    print("Error: List index is out of range.")

except ValueError:
    print("Error: Please enter an integer.")


# Example 3: Handle missing dictionary key
student = {"name": "Ali", "age": 20}

try:
    print("Marks =", student["marks"])

except KeyError:
    print("Error: The requested key does not exist.")
