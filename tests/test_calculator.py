"""Unit tests for the Operation class in the calculator module."""
import sys
#from unittest.mock import patch
from io import StringIO
import pytest
from calculator.operation import Operation
from calculator.calculate import Calculation
from calculator import calculator_repl


def run_calculator_with_input(monkeypatch, inputs):
    """
    Simulates user input and captures output from the calculator REPL.
    
    :param monkeypatch: pytest fixture to simulate user input
    :param inputs: list of inputs to simulate
    :return: captured output as a string
    """
    input_iterator = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iterator))

    # Capture the output of the calculator
    captured_output = StringIO()
    sys.stdout = captured_output
    calculator_repl()
    sys.stdout = sys.__stdout__  # Reset stdout
    return captured_output.getvalue()

# Positive Tests
def test_addition(monkeypatch):
    """Test addition operation in REPL."""
    inputs = [
        "1",  # Select addition
        "2",  # Enter first number
        "3",  # Enter second number
        "5",  # Exit
    ]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result of addition" in output


def test_subtraction(monkeypatch):
    """Test subtraction operation in REPL."""
    inputs = [
        "2",  # Select subtraction
        "5",  # Enter first number
        "3",  # Enter second number
        "5",  # Exit
    ]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result of subtraction" in output


def test_multiplication(monkeypatch):
    """Test multiplication operation in REPL."""
    inputs = [
        "3",  # Select multiplication
        "4",  # Enter first number
        "5",  # Enter second number
        "5",  # Exit
    ]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result of multiplication" in output


def test_division(monkeypatch):
    """Test division operation in REPL."""
    inputs = [
        "4",  # Select division
        "10",  # Enter first number
        "2",  # Enter second number
        "5",  # Exit
    ]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result of division" in output

def test_division_by_zero(monkeypatch):
    """Test division by zero in REPL."""
    inputs = [
        "4",  # Select division
        "5",  # Enter first number
        "0",  # Enter second number (division by zero)
        "5",  # Exit
    ]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Error: Cannot divide by zero." in output

def test_view_history(monkeypatch):
    """Test view history functionality in REPL."""
    inputs = [
        "1",  # Select addition
        "2",  # Enter first number
        "3",  # Enter second number
        "6",  # View history
        "5",  # Exit
    ]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Past Calculations" in output
    assert "Result of addition" in output

def test_clear_history(monkeypatch):
    """Test clear history functionality in REPL."""
    inputs = [
        "1",  # Select addition
        "2",  # Enter first number
        "3",  # Enter second number
        "7",  # Clear history
        "6",  # View history (should be empty)
        "5",  # Exit
    ]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Calculation history cleared." in output
    assert "Past Calculations" in output  # Should show empty history

def test_invalid_option(monkeypatch):
    """Test selecting an invalid operation in the REPL."""
    inputs = [
        "8",  # Invalid option
        "1",  # Valid option (addition)
        "2",  # Enter first number
        "3",  # Enter second number
        "5",  # Exit
    ]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Invalid choice. Please select a number between 1 and 7." in output

def test_non_numeric_input(monkeypatch):
    """Test non-numeric input handling in REPL."""
    inputs = [
        "1",  # Select addition
        "a",  # Invalid first number input
        "1",
        "3",
        "2",
        "5",
        #"2",  # Valid second number
        #"5",  # Exit
    ]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Error: Invalid input. Please enter numerical values." in output




@pytest.mark.parametrize("method, a, b, expected", [
    (Operation.add, 2, 2, 4),
    (Operation.subtract, 5, 2, 3),
    (Operation.multiply, 4, 5, 20),
    (Operation.divide, 10, 2, 5),
])
def test_operations(method, a, b, expected):
    """Test arithmetic operations."""
    assert method(a, b) == expected, f"Expected {expected} but got {method(a, b)}"


# Test division by zero
def test_divide_by_zero():
    """Test that division by zero raises ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Operation.divide(2, 0)


# Test non-integer division
def test_divide_non_integer():
    """Test that division returns the correct result for floating point numbers."""
    result = Operation.divide(5, 2)
    assert result == 2.5, f"Expected 2.5 but got {result}"


# Test invalid operation
def test_invalid_operation():
    """Test for invalid operations."""
    with pytest.raises(TypeError):
        Operation.add("string", 2)
    with pytest.raises(TypeError):
        Operation.subtract(2, "string")
    with pytest.raises(TypeError):
        Operation.multiply("string", "string")


# Test calculation history
def test_calculation_history():
    """Test calculation history functionality."""
    Calculation.clear_history()
    assert len(Calculation.get_history()) == 0
    Calculation("Addition", 2, 3, 5)
    assert len(Calculation.get_history()) == 1
    assert str(Calculation.get_last_calculation()) == "Addition: 2 and 3 = 5"


# Test clearing calculation history
def test_clear_calculation_history():
    """Test clearing calculation history."""
    Calculation("Addition", 1, 1, 2)
    Calculation.clear_history()
    assert not Calculation.get_history(), "History should be empty."


# Test the get_history when no calculations are added
def test_get_history_empty():
    """Test that get_history returns an empty list when no calculations have been added."""
    Calculation.clear_history()
    assert not Calculation.get_history(), "History should be empty."


# Test that add_calculation explicitly adds a calculation to history
def test_add_calculation():
    """Test that add_calculation correctly adds a calculation to history."""
    Calculation.clear_history()
    calc = Calculation("Multiplication", 3, 3, 9)
    # Now, add_calculation should only add the calculation once
    Calculation.add_calculation(calc)
    # Since the constructor already added the calculation, we expect the history to have only 1 item
    assert Calculation.get_history(), "History should not be empty."
    assert Calculation.get_history()[0] == calc, "item should match the added calculation."
