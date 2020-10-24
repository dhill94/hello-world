plainText = input("Enter the text you want to encrypt: ")
distance = int(input("Enter the distance value: "))
plainText = plainText.lower()
noSpace = plainText.replace(" ", "")

encrypted = ""

for ch in noSpace:
    ov = ord(ch)
    ev = ov + distance
    if ev > ord('z'):
            ev = ord('a') + distance - (ord('z') - ov + 1)
    encrypted += chr(ev)
print("Encrypted message:", encrypted)

