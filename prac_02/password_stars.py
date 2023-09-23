PASSWORD_LENGTH_THRESHOLD = 8


def main():
    password = get_password()
    print_asterisks(password)
    print("Password set")


def get_password():
    password = input("Enter password: ")
    while len(password) < PASSWORD_LENGTH_THRESHOLD:
        print("Password must be 8 characters or more long.")
        password = input("Enter password: ")
    return password


def print_asterisks(password):
    print(len(password) * "*")


main()
