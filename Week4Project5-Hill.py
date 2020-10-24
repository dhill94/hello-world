import math

org = int(input("Enter the amount of initial organisms: "))

rate = float(input("Enter the rate of growth: "))
while rate <= 0:
    rate = float(input("Please enter a valid number for rate of growth: "))

hoursRate = float(input("Enter the amount of hours it takes to achieve the rate of growth: "))
hoursGrowth = float(input("Enter the amount of hours during which the population grows: "))

growth = org * int(math.pow(rate, hoursGrowth//hoursRate))

print(growth)
