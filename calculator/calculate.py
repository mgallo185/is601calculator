"""Stores individual calculations."""

class Calculation:
    """Represents a single mathematical operation performed."""

    def __init__(self, operation: str, a: float, b: float, result: float):
        self.operation = operation
        self.a = a
        self.b = b
        self.result = result

    def __str__(self):
        """Return a string representation of the calculation."""
        return f"{self.operation}: {self.a} and {self.b} = {self.result}"
