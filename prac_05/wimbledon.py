"""
Game, Set, Match
Estimate: 45 minutes
Actual:   93 minutes
"""

FILENAME = "wimbledon.csv"


def main():
    records = get_records(FILENAME)
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count, countries)


def get_records(filename):
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def process_records(records):
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[1])
        if record in champion_to_count:
            champion_to_count[record[2]] += 1
        else:
            champion_to_count[record[2]] = 1
    return champion_to_count, countries


def display_results(champion_to_count, countries):
    print("Wimbledon Champions: ")
    for name, count in champion_to_count.items():
        print(name, count)
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(country for country in sorted(countries)))


main()
