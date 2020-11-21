"""Opening the file with numbers and splitting them into a list"""
def getNum(filename):
    with open(filename, 'r') as f:
        strList = f.read().split('\n')
        numList = [int(num) for num in strList]
    return numList

"""Returning the average of the acquired list"""
def getAvg(filename, func):
    numbers = func(filename)
    return sum(numbers)/len(numbers)

"""Using the functions to print the average"""
def main():
    filename = input("Enter name of file with numbers: ")
    average = getAvg(filename, getNum)
    print("The average of the numbers provided in the file is: " + str(round(average, 2)))

if __name__ == "__main__":
    main()
    
