import math
number = int(input("Enter the numeric grade: "))
if number > 100 or number < 0:
    print("Error: grade must be between 100 and 0")
else:
    square = math.sqrt(number)
    print("The square root of", number, "is", square)
