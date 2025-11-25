# Ian O'Neill
# IT 410
# Week 8 - While Loops Assignment
# Professor Charnesky

# list to store employee dictionaries
employees = []

# loop for up to 5 employees
for count in range(5):

    # ask for employee ID
    employee_id = input("Enter Employee ID: ")

    # check ID rules
    while not employee_id.isdigit() or len(employee_id) > 7:
        print("Invalid Employee ID. Please try again.")
        employee_id = input("Enter Employee ID: ")

    # check name rules
    while any(char in invalid_name_chars for char in employee_name):
        print("Invalid Employee Name. Please try again.")
        employee_name = input("Enter Employee Name: ")

    # ask for email
    employee_email = input("Enter Employee Email: ")

    # characters not allowed in email
    invalid_email_chars = '!\"\'#$%^&*()=+,<>/?;:[]{}\\'

    # check email rules
    while any(char in invalid_email_chars for char in employee_email):
        print("Invalid Email Address. Please try again.")
        employee_email = input("Enter Employee Email: ")

    # ask for address (optional)
    employee_address = input("Enter Employee Address (optional): ")

    # characters not allowed in address
    invalid_address_chars = '!\"\'@$%^&*_+=<>?;:[]{}'

    # check address only if provided
    while employee_address != "" and any(char in invalid_address_chars for char in employee_address):
        print("Invalid Address. Please try again.")
        employee_address = input("Enter Employee Address (optional): ")