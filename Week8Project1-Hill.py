import math

def newton(x):
    """Newtons method for approximating square roots."""

    # Initialize the tolerance and estimate
    tolerance = 0.000001
    estimate = 1.0

    # Perform the successive approximations
    while True:
         estimate = (estimate + x / estimate) / 2
         difference = abs(x - estimate ** 2)
         if difference <= tolerance:
             break
    return estimate


def main():
    while True:
        #Asking for users input, only taking positive numbers
        x = input("\nEnter a positive number or enter/return to quit: ")
        if not str(x):
            break
        elif float(x) < 0:
            x = input("\nYou have entered an invalid number, please enter a positive number or enter/return to quit: ")
            if not str(x):
                break
        x = float(x)
        #Printing the results
        print("The program's estimate is", newton(x))
        print("Python's estimate is     ", math.sqrt(x))

if __name__ == "__main__":
    main()
