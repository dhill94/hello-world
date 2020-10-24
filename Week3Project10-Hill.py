wage = input("Enter your hourly wage: ")
regHours = input("Enter how many regular hours you worked: ")
otHours = input("Enter your overtime hours: ")

reg = float(regHours) * float(wage)
ot = float(otHours) * (float(wage) * 1.5)
total = float(reg) + float(ot)

print("Your total weekly pay is: $" + str(round(total, 2)))
