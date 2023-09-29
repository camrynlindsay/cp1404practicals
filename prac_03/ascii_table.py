LOWER_BOUND = 33
UPPER_BOUND = 127


def main():
    character = get_valid_character()
    number = get_valid_number()
    print(f"The ASCII code for {character} is {convert_string_to_ascii_code(character)}")
    print(f"The character for {number} is {convert_integer_to_ascii_code(number)}")


def get_valid_character():
    character = input("Enter a character: ")
    while character.isdigit():
        print("Invalid input")
        character = input("Enter a character: ")
    return character


def get_valid_number():
    number = int(input(f"Enter a number between "))
    while LOWER_BOUND > number or number > UPPER_BOUND:
        print(f"Invalid number. Please choose a number between {LOWER_BOUND} amd {UPPER_BOUND}")
        number = int(input(f"Enter a number between "))
    return number


def convert_string_to_ascii_code(character):
    return ord(character)



def convert_integer_to_ascii_code(number):
    return chr(number)



main()
