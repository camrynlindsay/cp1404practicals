"""
Emails
Estimate: 30 minutes
Actual:  29 minutes
"""


def main():
    """Ask the user for their email and print a dictionary of their name to email"""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ")
        if confirmation.upper() != "" and confirmation != "Y":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for name, email in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    """Split the name from the email"""
    prefix = email.split("@")[0]
    parts = prefix.split(".")
    name = " ".join(parts).title()
    return name


main()
