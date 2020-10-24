initialHeight = float(input("Enter the initial height of the drop in feet: "))
bounce = int(input("Enter how many times the ball is allowed to bounce: "))
bounceHeight = initialHeight * 0.6
height = initialHeight
distance = 0


for count in range(bounce):
    distance = distance + height + bounceHeight
    height = bounceHeight
    bounceHeight = bounceHeight * 0.6


print("The total distance traveled is: %0.2f" % distance + " ft")
