PASSWORD_LENGTH_THRESHOLD = 8


def main():
    """This programs asks a user for a valid password and prints out asteriks based on
    the length of the password"""
    password = get_password()
    print_asterisks(password)


def get_password():
    """Get a valid password from user"""
    password = input("Enter password: ")
    while len(password) < PASSWORD_LENGTH_THRESHOLD:
        print("Password must be 8 characters or more long.")
        password = input("Enter password: ")
    return password


def print_asterisks(password):
    """Print asteriks based on the length of the password input"""
    print(len(password) * "*")


main()
