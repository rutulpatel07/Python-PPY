fname = input("First Name: ")
lname = input("Last Name: ")
year = input("Birth Year: ")

email = f"{fname}.{lname}@uvpce.edu.in"
username = f"{lname}_{fname}{year[-2:]}"

print("Email:", email)
print("Username:", username)
