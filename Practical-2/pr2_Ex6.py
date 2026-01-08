P = float(input("Principal: "))
R = float(input("Rate: "))
T = float(input("Time (months): "))

SI = (P * R * T) / 100
Total = P + SI

print("Simple Interest:", SI)
print("Total Amount:", Total)
