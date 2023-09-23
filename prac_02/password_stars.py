PASSWORD_LENGTH_THRESHOLD = 8

password = input("Enter password: ")
while len(password) < PASSWORD_LENGTH_THRESHOLD:
    print("Password must be 8 characters or more long.")
    password = input("Enter password: ")
print(len(password) * "*")
print("Password set")
