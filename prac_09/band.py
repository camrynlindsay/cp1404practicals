"""
Band Association
Estimate: 45 minutes
Actual: 36 minutes
"""


class Band:
    """Band class."""

    def __init__(self, name):
        """Construct values for a Band instance."""
        self.name = name
        self.instruments = []
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing the musician/s playing their first instrument."""
        results = []
        for musician in self.musicians:
            results.append(musician.play())
        return "\n".join(results)
