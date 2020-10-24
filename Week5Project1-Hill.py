side1 = int(input("Enter the length of the triangles left side: "))
side2 = int(input("Enter the length of the triangles right side: "))
side3 = int(input("Enter the length of the triangles bottom side: "))

if side1 == side2 and side2 == side3:
    print("This is an equilateral triangle.")
else:
    print("This is not an equilateral triangle.")
