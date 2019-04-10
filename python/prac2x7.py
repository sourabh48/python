a = input("Enter a character: ")
asciival = ord(a)

if asciival >= 65 and asciival <= 90:
    print("Capital Letter")
elif asciival >= 97 and asciival <= 122:
    print("Small Letter")
elif asciival >= 48 and asciival <=52:
    print("Numericals")    
else:
    print("Special character")