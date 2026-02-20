students = {
    "male": ["Tom", "Charlie", "Harry", "Frank"],
    "female": ["Sarah", "Huda", "Samantha", "Emily", "Elizabeth"]
}

for group in students:
    for name in students[group]:
        if 'a' in name.lower():
            print(name)
