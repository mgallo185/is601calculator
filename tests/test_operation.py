"""testing operations """
import pytest
from calculator.operation import Operation

@pytest.mark.parametrize("method, a, b, expected", [
    (Operation.add, 2, 2, 4),
    (Operation.subtract, 5, 2, 3),
    (Operation.multiply, 4, 5, 20),
    (Operation.divide, 10, 2, 5),
])
def test_calculations(method, a, b, expected):
    """Test arithmetic operations."""
    assert method(a, b) == expected, f"Expected {expected} but got {method(a, b)}"

def test_divide_by_zero():
    """Test that division by zero raises ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Operation.divide(2, 0)

def test_divide_non_integer():
    """Test that division returns the correct result for floating point numbers."""
    result = Operation.divide(5, 2)
    assert result == 2.5, f"Expected 2.5 but got {result}"

def test_invalid_operation():
    """Test for invalid operations."""
    with pytest.raises(TypeError):
        Operation.add("string", 2)
    with pytest.raises(TypeError):
        Operation.subtract(2, "string")
    with pytest.raises(TypeError):
        Operation.multiply("string", "string")
