FILENAME = "name.txt"
NUMBER_FILE = "numbers.txt"

# Question 1
name = input("Name: ")
out_file = open(FILENAME, "w")
print(name, file=out_file)
out_file.close()

# Question 2
input_file = open(FILENAME, 'r')
text = input_file.read()
input_file.close()
print(f"Your name is {text}")

# Question 3
input_file = open(NUMBER_FILE, 'r')
first_number = int(input_file.readline().strip())
second_number = int(input_file.readline().strip())
input_file.close()
result = first_number + second_number
print(result)

# Question 4
result = 0
input_file = open(NUMBER_FILE, 'r')
for line in input_file:
    numbers_in_file = int(line.strip())
    result += numbers_in_file
input_file.close()
print(result)
