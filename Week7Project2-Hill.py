fileName = input("Enter the filename: ")
f = open(fileName, 'r')

lines = []
for line in f:
    lines.append(line)
    
print("There are", len(lines), "lines in the document.")
x = int(input("Please type the number of the line you wish to view or type 0 to quit: "))
while x >= 0:
    if x > 0 and x <= len(lines):
        print("\nLine", x, ": ", lines[x - 1])
        x = int(input("If you wish to view another line please type the number or 0 to quit: "))
    elif x > len(lines):
        x = int(input("That line doesn't exist. Please enter the line number you wish to view or 0 to quit: "))
    elif x == 0:
        print("The program has ended.")
        break
