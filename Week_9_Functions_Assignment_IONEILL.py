# Ian O'Neill
# IT 410
# Week 9 - Functions Assignment
# Professor Charnesky

# function to get valid input
def get_valid_input(prompt, invalid_chars, max_len=None, digits_only=False):
    user_input = input(prompt)

    # loop for checking
    while True:
        # check digits only
        if digits_only and not user_input.isdigit():
            print("Invalid input. Try again.")
        # check length
        elif max_len and len(user_input) > max_len:
            print("Too long. Try again.")
        # check invalid chars
        elif any(char in invalid_chars for char in user_input):
            print("Invalid input. Try again.")
        else:
            break

        user_input = input(prompt)

    return user_input

# function for optional input
def get_optional_input(prompt, invalid_chars):
    user_input = input(prompt)

    # only check if something typed
    while user_input != "" and any(char in invalid_chars for char in user_input):
        print("Invalid input. Try again.")
        user_input = input(prompt)

    return user_input

employees = []

# loop for up to 5 employees
for count in range(5):

    # getting id
    employee_id = get_valid_input(
        "Enter Employee ID: ",
        invalid_chars="",
        max_len=7,
        digits_only=True
    )

    # getting name
    employee_name = get_valid_input(
        "Enter Employee Name: ",
        invalid_chars='!"@#$%^&*()_=+,<>/?;:[]{}\\'
    )

    # getting email
    employee_email = get_valid_input(
        "Enter Employee Email: ",
        invalid_chars='!"\'#$%^&*()=+,<>/?;:[]{}\\'
    )

    # getting address
    employee_address = get_optional_input(
        "Enter Employee Address (optional): ",
        invalid_chars='!"\'@$%^&*_+=<>?;:[]{}'
    )

    # storing employee
    employee_record = {
        "id": employee_id,
        "name": employee_name,
        "email": employee_email,
        "address": employee_address
    }

    employees.append(employee_record)

    # ask to continue
    more = input("Add another employee? (yes/no): ").lower()
    if more != "yes":
        break

print("\nFinal Employee List:")
print(employees)
