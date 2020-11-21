numbers = []
x = int(input("How many numbers are in the list? "))
if x > 0:
    print("Please enter the numbers: ")

for i in range(0, x):
    num = int(input())
    numbers.append(num)

numbers.sort()

def median(numbers):
    mid = len(numbers) // 2
    if len(numbers) % 2 == 1:
        return numbers[mid]
    else:
        return (numbers[mid] + numbers[mid - 1]) / 2

def mode(numbers):
    d = {}
    for i in numbers:
        if not i in d:
            d[i] = 1
        else:
            d[i] += 1
    return [k for k,v in d.items() if v==max(d.values())]


def mean(numbers):
    theSum = 0
    for number in numbers:
        theSum += number
    return round((theSum / len(numbers)), 2)

def main():
    if x == 0:
        print("\nThe list provided was: 0")
        print("The median of the list provided is: 0")
        print("The mode of the list provided is: 0")
        print("The mean of the list provided is: 0")
    else: 
        print("\nThe list provided was:", numbers)
        print("The median of the list provided is:", median(numbers))
        print("The mode of the list provided is:", ','.join(map(str, mode(numbers))))
        print("The mean of the list provided is:", mean(numbers))

if __name__ == "__main__":
    main()
