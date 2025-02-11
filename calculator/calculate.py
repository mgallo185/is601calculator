"""Stores individual calculations."""

class Calculation:
    """Represents a single mathematical operation performed."""
    # store calcualtion history
    history = [] 
    
    def __init__(self, operation: str, a: float, b: float, result: float):
        self.operation = operation
        self.a = a
        self.b = b
        self.result = result
        Calculation.history.append(self)

    def __str__(self):
        """Return a string representation of the calculation."""
        return f"{self.operation}: {self.a} and {self.b} = {self.result}"
    
    @classmethod
    def get_history(cls):
        """Returns the full calculation history."""
        return cls.history

    @classmethod
    def clear_history(cls):
        """Clears all stored calculations from history."""
        cls.history.clear()

    @classmethod
    def get_last_calculation(cls):
        """Returns the most recent calculation, or None if history is empty."""
        return cls.history[-1] if cls.history else None
    
    @classmethod
    def add_calculation(cls, calculation):
        """Adds a calculation to history explicitly."""
        cls.history.append(calculation)
