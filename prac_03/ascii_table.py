LOWER_BOUND = 33
UPPER_BOUND = 127


def main():

    character = input("Enter a character: ")

    number = get_valid_number()
    ascii_code = convert_integer_to_ascii_code(number)
    print(number)
    print(ascii_code)


def get_valid_number():
    number = int(input(f"Enter a number between "))
    while LOWER_BOUND > number or number > UPPER_BOUND:
        print(f"Invalid number. Please choose a number between {LOWER_BOUND} amd {UPPER_BOUND}")
        number = int(input(f"Enter a number between "))
    return number


def convert_string_to_ascii_code(character):
    ascii_code = ord(character)
    return ascii_code


def convert_integer_to_ascii_code(number):
    ascii_code = chr(number)
    return ascii_code


main()
