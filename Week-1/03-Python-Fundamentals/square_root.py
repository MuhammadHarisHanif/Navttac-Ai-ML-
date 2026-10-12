# Task 4: Calculate Square Root

import math

num = float(input("Enter a number: "))

if num >= 0:
    result = math.sqrt(num)
    print("Square root =", result)
else:
    result = math.sqrt(abs(num))
    print("Square root =", result, "i")
