FILENAME = "name.txt"

# Question 1
name = input("Name: ")
out_file = open(FILENAME, "w")
print(name, file=out_file)
out_file.close()

# Question 2
in_file = open(FILENAME, 'r')
text = in_file.read()
in_file.close()
print(f"Your name is {text}")

