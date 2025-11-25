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
