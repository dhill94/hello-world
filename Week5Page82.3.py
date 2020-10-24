import math
number = int(input("Enter the numeric grade: "))
if number >= 0 and number <= 100:
    square = math.sqrt(number)
    print("The square root of", number, "is", square)
else:
    print("Error: grade must be between 100 and 0")
