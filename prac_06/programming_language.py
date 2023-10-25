class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, year):
        """Initialise values about a ProgrammingLanguage."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if a ProgrammingLanguage is typed dynamically."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Represent the string of a ProgrammingLanguage."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
