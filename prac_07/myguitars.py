from guitar import Guitar

FILENAME = "guitars.csv"

guitars = []

with open(FILENAME, 'r') as in_file:
    for line in in_file:
        parts = line.strip().split(",")
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
for guitar in guitars:
    print(guitar)