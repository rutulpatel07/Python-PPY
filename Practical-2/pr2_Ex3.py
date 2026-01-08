import math

r = float(input("Radius: "))
h = float(input("Height: "))

volume = math.pi * r * r * h
surface = 2 * math.pi * r * (r + h)

print("Volume:", volume)
print("Surface Area:", surface)
