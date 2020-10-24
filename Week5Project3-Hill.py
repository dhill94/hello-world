import random
import math
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
while larger <= smaller:
    larger = int(input("Enter a number higher than " + str(smaller) + " : "))
number = input("Enter a number between " + str(smaller) + " and " + str(larger) + " : ")
number = int(number)
low = smaller
high = larger

while number <= smaller or number >= larger:
    number = input("Please enter a valid number between " + str(smaller) + " and " + str(larger) + " : ")
    number = int(number)
else:
    print("\nComputer has ", round(math.log(larger - smaller + 1, 2))," chances to guess.\n")

count = 0
while count < round(math.log(larger - smaller + 1, 2)):
    count += 1
    
    guess = random.randint(low, high)
    if guess < number:
        print("The computer guessed:", guess)
        low = guess + 1
        guess = random.randint(low, high)
    elif guess > number:
        print("The computer guessed:", guess)
        high = guess - 1
        guess = random.randint(low, high)
    elif guess == number:
        print("The computer guessed:", guess)
        print("\nThe computer got it in", count, "tries!")
        break

count += 1
if count > round(math.log(larger - smaller + 1, 2)):
    print("\nThe computer did not guess the number in the amount of tries available.")
