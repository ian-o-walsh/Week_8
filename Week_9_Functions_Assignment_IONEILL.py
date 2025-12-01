# Ian O'Neill
# IT 410
# Week 9 - Functions Assignment
# Professor Charnesky

def get_valid_input(prompt, invalid_chars, max_len=None, digits_only=False):
    user_input = input(prompt)

    # loop for checking
    while True:
        if digits_only and not user_input.isdigit():
            print("Invalid input. Try again.")
        elif max_len and len(user_input) > max_len:
            print("Too long. Try again.")
        elif any(char in invalid_chars for char in user_input):
            print("Invalid input. Try again.")
        else:
            break

        user_input = input(prompt)

    return user_input

# list to store employee dictionaries
employees = []

# function for optional input
def get_optional_input(prompt, invalid_chars):
    user_input = input(prompt)

    # only check if something typed
    while user_input != "" and any(char in invalid_chars for char in user_input):
        print("Invalid input. Try again.")
        user_input = input(prompt)

    return user_input