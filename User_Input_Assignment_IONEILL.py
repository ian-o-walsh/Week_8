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
