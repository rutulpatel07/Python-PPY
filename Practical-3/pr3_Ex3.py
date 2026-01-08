st = input("Enter string: ")
new = ""

for ch in st:
    if ch.lower() in 'aeiou':
        new += '*'
    elif ch.isdigit():
        new += '#'
    elif ch == ' ':
        new += '_'
    else:
        new += ch

print("Original:", st)
print("Modified:", new)
