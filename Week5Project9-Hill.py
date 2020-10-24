theSum = 0.0
theAvg = 0.0
count = 0

while True:
    data = input("Enter a number or just enter to quit: ")
    if data == "":
        break
    number = float(data)
    theSum += number
    count += 1
theAvg = theSum / count
print("The sum is", theSum, "and the average is", theAvg)
