FILENAME = "name.txt"

# Question 1
# name = input("Name: ")
# out_file = open(FILENAME, "w")
# print(name, file=out_file)
# out_file.close()

# Question 2
# in_file = open(FILENAME, 'r')
# text = in_file.read()
# in_file.close()
# print(f"Your name is {text}")

# Question 3
input_file = open("numbers.txt", 'r')
first_number = int(input_file.readline().strip())
second_number = int(input_file.readline().strip())
result = first_number + second_number
print(result)
