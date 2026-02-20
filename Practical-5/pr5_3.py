d = {"a":1, "b":2, "c":3, "d":5}

new_d = {}

for key, value in d.items():
    if value <= 2:
        new_d[key] = value

print(new_d)
