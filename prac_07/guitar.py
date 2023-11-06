CURRENT_YEAR = 2023
VINTAGE_AGE = 50


class Guitar:
    """Represent information about a guitar."""

    def __init__(self, name="", year=0, cost=0.0):
        """Initialise values about a guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string of a representation of a guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,}"

    def get_age(self):
        """Get the age of a guitar."""
        age = CURRENT_YEAR - self.year
        return age

    def is_vintage(self):
        """Determine if a guitar is considered vintage."""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """Determine if a guitar older than another guitar."""
        return self.year < other.year
