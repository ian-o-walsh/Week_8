# Ian O'Neill
# IT 410
# Week 8 - User Input Assignment
# Professor Charnesky

# ask for employee ID
employee_id = input("Enter Employee ID: ")

# check ID rules
if not employee_id.isdigit() or len(employee_id) > 7:
    print("Invalid Employee ID. Program ending.")
    exit()

# ask for employee name
employee_name = input("Enter Employee Name: ")

# characters not allowed in name
invalid_name_chars = '!\"@#$%^&*()_=+,<>/?;:[]{}\\'

# check name rules
for char in employee_name:
    if char in invalid_name_chars:
        print("Invalid Employee Name. Program ending.")
        exit()

# ask for email
employee_email = input("Enter Employee Email: ")

# characters not allowed in email
invalid_email_chars = '!\"\'#$%^&*()=+,<>/?;:[]{}\\'

# check email rules
for char in employee_email:
    if char in invalid_email_chars:
        print("Invalid Email Address. Program ending.")
        exit()

# ask for address
employee_address = input("Enter Employee Address (optional): ")

# characters not allowed in address
invalid_address_chars = '!\"\'@$%^&*_+=<>?;:[]{}'

# check address only if provided
if employee_address != "":
    for char in employee_address:
        if char in invalid_address_chars:
            print("Invalid Address. Program ending.")
            exit()
            
# final output
print()
print("Hello,", employee_name + ". Your Employee ID is", employee_id + ", and your email address is", employee_email + ".")

if employee_address == "":
    print("You did not provide an address.")
else:
    print("Your address is", employee_address + ".")