marks = []
for i in range(5):
    marks.append(int(input(f"Enter marks {i+1}: ")))

percentage = sum(marks) / 5

if percentage >= 90:
    grade = 'A'
elif percentage >= 80:
    grade = 'B'
elif percentage >= 70:
    grade = 'C'
elif percentage >= 60:
    grade = 'D'
else:
    grade = 'F'

print("Percentage:", percentage)
print("Grade:", grade)
