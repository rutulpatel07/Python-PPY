a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

odds = []

if a % 2 != 0:
    odds.append(a)
if b % 2 != 0:
    odds.append(b)
if c % 2 != 0:
    odds.append(c)

print("Odd count:", len(odds))
if odds:
    print("Maximum odd number:", max(odds))
else:
    print("No odd numbers")
