""" Testnig repl """
import sys
from io import StringIO
import pytest
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


@pytest.mark.parametrize("operation, num1, num2, expected", [
    ("1", 2, 3, "Result of addition"),
    ("2", 5, 3, "Result of subtraction"),
    ("3", 4, 5, "Result of multiplication"),
    ("4", 10, 2, "Result of division"),
])

def test_operations(monkeypatch, operation, num1, num2, expected):
    """Test various arithmetic operations in REPL."""
    inputs = [
        operation,  # Select operation
        str(num1),  # Enter first number
        str(num2),  # Enter second number
        "5",  # Exit
    ]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert expected in output

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
