"""Unit tests for the Operation class in the calculator module."""

import sys
from io import StringIO
import pytest
from calculator.operation import Operation
from calculator import calculator_repl




def calculator_input(monkeypatch,inputs):
    """ testing repl input via monkey patch"""
    input_iterator = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iterator))

    captured_output = StringIO()
    sys.stdout = captured_output  # Redirect stdout
    calculator_repl()  # Run the REPL calculator
    sys.stdout = sys.__stdout__  # Reset stdout
    return captured_output.getvalue()


def test_addition(monkeypatch):
    """Test addition operation in REPL."""
    inputs = ["1", "2", "3", "5"]  # Selects Addition, inputs 2 and 3, then exits
    output = calculator_input(monkeypatch, inputs)
    assert "Result of addition: 5.0" in output


def test_subtraction(monkeypatch):
    """Test subtraction operation in REPL."""
    inputs = ["2", "5", "2", "5"]
    output = calculator_input(monkeypatch, inputs)
    assert "Result of subtraction: 3.0" in output


def test_multiplication(monkeypatch):
    """Test multiplication operation in REPL."""
    inputs = ["3", "4", "5", "5"]
    output = calculator_input(monkeypatch, inputs)
    assert "Result of multiplication: 20.0" in output


def test_division(monkeypatch):
    """Test division operation in REPL."""
    inputs = ["4", "10", "2", "5"]
    output = calculator_input(monkeypatch, inputs)
    assert "Result of division: 5.0" in output


def test_invalid_choice(monkeypatch):
    """Test invalid menu choice in REPL."""
    inputs = ["9", "5"]  # Invalid choice, then exit
    output = calculator_input(monkeypatch, inputs)
    assert "Invalid choice. Please select a number between 1 and 5." in output


def test_division_by_zero(monkeypatch):
    """Test division by zero in REPL."""
    inputs = ["4", "5", "0", "5"]
    output = calculator_input(monkeypatch, inputs)
    assert "Error: Cannot divide by zero." in output


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
