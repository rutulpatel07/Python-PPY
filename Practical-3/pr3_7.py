st = input("Enter string: ")

digits = upper = lower = 0

for ch in st:
    if ch.isdigit():
        digits += 1
    elif ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Digits:", digits)
print("Uppercase:", upper)
print("Lowercase:", lower)
