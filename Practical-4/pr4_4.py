# 1) In same list
L = [8,5,2,9,11,40,1]

L.sort()
print("In same list sort:")
print(L)

# 2) Create sorted copy of original list & print both
L1 = [20,40,19,32,9]

LC =sorted(L1)
print("With Copy method:")
print("Original List:",L1)
print("Sorted List:",LC)

#3) Sort without any built-in function

L2 = [5,4,1,8,6]
n = len(L2)
for i in range(n-1):
    for j in range(n-i-1):
        if(L2[j]>L2[j+1]):
            L2[j],L2[j+1] = L2[j+1],L2[j]

print("Sort without builtin method:")
print(L2)
