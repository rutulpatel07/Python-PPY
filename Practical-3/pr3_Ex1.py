n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    if a > 999:
        break

    if a < 10:
        print(f"00{a}")
    elif a < 100:
        print(f"0{a}")
    else:
        print(a)

    c = a + b
    a = b
    b = c
