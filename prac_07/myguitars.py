from guitar import Guitar
import csv

FILENAME = "guitars.csv"

guitars = []

# with open(FILENAME, 'r') as in_file:
#     for line in in_file:
#         parts = line.strip().split(",")
#         guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
#         guitars.append(guitar)

name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    new_guitar = Guitar(name, year, cost)
    guitars.append(new_guitar)
    name = input("Name: ")

guitars.sort()
for guitar in guitars:
    print(f"{guitar.name:25} ({guitar.year}) : ${guitar.cost}")

with open(FILENAME, 'w', newline='') as out_file:
    writer = csv.writer(out_file)
    for guitar in guitars:
        writer.writerow([guitar.name, guitar.year, guitar.cost])
