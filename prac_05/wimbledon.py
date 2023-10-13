"""
Game, Set, Match
Estimate: 45 minutes
Actual:   93 minutes
"""

FILENAME = "wimbledon.csv"


def main():
    """Read, process and display the information from the wimbledon file."""
    records = get_records(FILENAME)
    champion_to_count, countries = process_records(records)
    display_records(champion_to_count, countries)


def get_records(filename):
    """Get the records from the input file."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def process_records(records):
    """Process the records into a set and dictionary."""
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[1])
        try:
            champion_to_count[record[2]] += 1
        except KeyError:
            champion_to_count[record[2]] = 1
    return champion_to_count, countries


def display_records(champion_to_count, countries):
    """Display the champions and countries."""
    print("Wimbledon Champions: ")
    for name, count in champion_to_count.items():
        print(name, count)
    print()
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(country for country in sorted(countries)))


main()
