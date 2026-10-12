

# NAVTTC AI/ML - Week 2
# Task 27: User-Defined Exception Handling

# Example 1: Create a custom exception
class InvalidAgeError(Exception):
    pass


try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise InvalidAgeError("Age cannot be negative.")

    print("Your age is:", age)

except InvalidAgeError as error:
    print("Custom Error:", error)

except ValueError:
    print("Error: Please enter a valid integer.")


# Example 2: Custom exception for marks
class InvalidMarksError(Exception):
    pass


try:
    marks = int(input("Enter marks (0-100): "))

    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100.")

    print("Your marks are:", marks)

except InvalidMarksError as error:
    print("Custom Error:", error)

except ValueError:
    print("Error: Please enter valid marks.")
