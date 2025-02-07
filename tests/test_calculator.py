"""Unit tests for the Operation class in the calculator module."""

import pytest
from calculator.operation import Operation

# Test arithmetic operations
@pytest.mark.parametrize("method, a, b, expected", [
    (Operation.add, 2, 2, 4),
    (Operation.subtract, 2, 2, 0),
    (Operation.multiply, 2, 2, 4),
    (Operation.divide, 2, 2, 1),
])
def test_operations(method, a, b, expected):
    """Test arithmetic operations"""
    assert method(a, b) == expected, f"Expected {expected} but got {method(a, b)}"

# Test division by zero
def test_divide_by_zero():
    """Test that division by zero raises ValueError"""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Operation.divide(2, 0)
