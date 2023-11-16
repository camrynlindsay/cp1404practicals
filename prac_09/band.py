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
        self.members = []

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.members)})"

    def add(self, member):
        """Add a member to the band."""
        self.members.append(member)

    def play(self):
        """"""
        pass
        # for member in self.members:
        #     if member
        #
        # return f"{self.name} is playing: {self.instruments[0]}"
        # if self.instruments:
        # return f"{self.name} is playing: {self.instruments[0]}"
