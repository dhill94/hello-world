iteration = int(input("Please enter the number of iterations: "))
total = 0
for i in range(iteration):
    total = total + (-1.0)**i/(2.0*i+1.0)
result = 4*total

print("The resulting value is: " + str(result))
