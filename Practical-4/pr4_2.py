l = [7, 4, 5, 4, 2, 7, 5, 8]
print("Using inbuilt Function:")
print("Maximum element is:",max(l))
print("Minimum element is:",min(l))

l1 = [8, 99, 4, 5, 10]

max = 0
min = 0
for i in l1:
    if i > max:
        max = i
    else:
        min = i
    
print("Using For Loop:")
print("Maximum element is:",max)
print("Minimum element is:",min)
