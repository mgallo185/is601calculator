"""testing operations """
import pytest
from calculator.operation import Operation
from faker import Faker

fake = Faker()

@pytest.mark.parametrize("method, a, b, expected", [
    (Operation.add, fake.random_int(min=1, max=100), fake.random_int(min=1, max=100), lambda a, b: a + b),
    (Operation.subtract, fake.random_int(min=1, max=100), fake.random_int(min=1, max=100), lambda a, b: a - b),
    (Operation.multiply, fake.random_int(min=1, max=10), fake.random_int(min=1, max=10), lambda a, b: a * b),
    (Operation.divide, fake.random_int(min=1, max=100), fake.random_int(min=1, max=10), lambda a, b: round(a / b, 2)),
])
def test_calculations(method, a, b, expected):
    """Test arithmetic operations using Faker-generated data."""
    result = method(a, b)
    expected_value = expected(a, b)
    
    if method == Operation.divide:
        # Use pytest.approx() for floating-point comparisons
        assert result == pytest.approx(expected_value, rel=1e-2), f"Expected {expected_value} but got {result}"
    else:
        assert result == expected_value, f"Expected {expected_value} but got {result}"

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
