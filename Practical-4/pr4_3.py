l1 = []
num = int(input("Enter the number: "))
for i in range(1,num+1):
    if num%i==0:
        l1.append(i)
print(l1)
