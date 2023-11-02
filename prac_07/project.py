class Project:
    """Represent information about a project."""

    def __init__(self, name="", start_date="", priority=0, cost_estimate=0, percentage=0):
        """Initialise values about a project."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.percentage = percentage

    def __repr__(self):
        """Return the string representation of the class Project."""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate}," \
               f" completion: {self.percentage}%"
