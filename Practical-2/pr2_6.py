days = int(input("Enter number of late days: "))
fine_paisa = 0

if days <= 5:
    fine_paisa = days * 40
elif days <= 10:
    fine_paisa = (5 * 40) + (days - 5) * 65
else:
    fine_paisa = (5 * 40) + (5 * 65) + (days - 10) * 80

fine_rupees = fine_paisa / 100

print("Total Fine in Paisa:", fine_paisa)
print("Total Fine in Rupees: ₹", fine_rupees)
