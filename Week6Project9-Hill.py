fileNameInput = input("Enter the name of the input file: ")
fileNameOutput = input("Enter the name of the output file: ")

count = 1

readFile = open(fileNameInput, 'r')
outputFile = open(fileNameOutput, 'w')

for lines in readFile:
    lines = lines.strip()
    outputFile.write(str(count) + '>' + ' ' + lines + '\n')
    count += 1
    
readFile.close()
outputFile.close()
