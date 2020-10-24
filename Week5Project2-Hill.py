import math
legA = float(input("Enter leg A of the triangle: "))
legB = float(input("Enter leg B of the triangle: "))
hyp = float(input("Enter the hypotenuse of the triangle: "))
side3 = math.sqrt((legA ** 2) + (legB ** 2))

if hyp == math.sqrt((legA ** 2) + (legB ** 2)):
    print("This is a right triangle.")
else:
    print("This is not a right triangle.")
