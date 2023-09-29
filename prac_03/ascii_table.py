LOWER_BOUND = 33
UPPER_BOUND = 127


def main():

    character = str(input("Enter a character: "))
    number = get_valid_number()


def get_valid_number():
    number = int(input(f"Enter a number between "))
    while LOWER_BOUND > number or number > UPPER_BOUND:
        print(f"Invalid number. Please choose a number between {LOWER_BOUND} amd {UPPER_BOUND}")
        number = int(input(f"Enter a number between "))
    return number


def convert_string_to_ascii_code():
    pass


def convert_integer_to_ascii_code():
    pass


main()
