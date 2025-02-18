""" Testing calculation class with its history"""
from calculator.calculate import Calculation
from faker import Faker

fake =Faker()
def test_calculation_history():
    """Test calculation history functionality."""
    Calculation.clear_history()
    assert len(Calculation.get_history()) == 0
    Calculation("Addition", 2, 3, 5)
    assert len(Calculation.get_history()) == 1
    assert str(Calculation.get_last_calculation()) == "Addition: 2 and 3 = 5"

def test_clear_calculation_history():
    """Test clearing calculation history."""
    Calculation("Addition", 1, 1, 2)
    Calculation.clear_history()
    assert not Calculation.get_history(), "History should be empty."

def test_get_history_empty():
    """Test that get_history returns an empty list when no calculations have been added."""
    Calculation.clear_history()
    assert not Calculation.get_history(), "History should be empty."

def test_add_calculation():
    """Test that add_calculation correctly adds a calculation to history with fake data."""
    Calculation.clear_history()
    a = fake.random_int(min=1, max=100)
    b = fake.random_int(min=1, max=100)
    result = a + b
    calc = Calculation("Addition", a, b, result)
    Calculation.add_calculation(calc)
    
    assert Calculation.get_history(), "History should not be empty."
    assert Calculation.get_history()[0] == calc, "Item should match the added calculation."
