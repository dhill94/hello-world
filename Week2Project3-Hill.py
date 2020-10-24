new = float(3.00)
old = float(2.00)

newAmount = float(input("Enter amount of new videos: "))
oldAmount = float(input("Enter amount of old videos: "))

total = (newAmount * new) + (oldAmount * old)

print(f'Total cost: ${total:.2f}')
