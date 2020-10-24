fileName = input("Enter the name of the file: ")
openFile = open(fileName, 'r')

print('Name'.ljust(15), 'Hours'.ljust(15), 'Wages Paid'.ljust(15))

for lines in openFile:
    split = lines.split()
    lastName = split[0]
    hourlyWage = split[1]
    hoursWorked = split[2]
    total = float(hourlyWage) * float(hoursWorked)
    print(str(lastName).ljust(15), str(hoursWorked).ljust(15), str(total).ljust(15))
    
