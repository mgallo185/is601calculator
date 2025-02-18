import pytest
from faker import Faker
from calculator.operation import Operation

fake = Faker()

def generate_test_cases(num_records):
    """Generate randomized test cases for operations using Faker."""
    test_cases = []
    for _ in range(num_records):
        a = fake.random_int(min=1, max=100)
        b = fake.random_int(min=1, max=100)

        test_cases.append((Operation.add, a, b, a + b))
        test_cases.append((Operation.subtract, a, b, a - b))

        # Fix multiplication by properly assigning random values
        mul_a = fake.random_int(min=1, max=10)
        mul_b = fake.random_int(min=1, max=10)
        test_cases.append((Operation.multiply, mul_a, mul_b, mul_a * mul_b))

        # Fix division by ensuring divisor is never zero
        div_b = fake.random_int(min=1, max=10)  # Always between 1-10
        test_cases.append((Operation.divide, a, div_b, round(a / div_b, 2)))

    return test_cases

def pytest_addoption(parser):
    """Add custom command-line option to pytest."""
    parser.addoption(
        "--num_records",
        action="store",
        default=10,  # Default value if not provided
        type=int,
        help="Number of test cases to generate"
    )

@pytest.fixture(scope="session")
def num_records(request):
    """Retrieve the number of test cases from the command-line option."""
    return request.config.getoption("--num_records")

@pytest.fixture(params=None)
def operation_test_data(request, num_records):
    """Fixture to provide Faker-generated test data for operations."""
    test_cases = generate_test_cases(num_records)
    request.param = test_cases[request.param_index]  # Assign param manually
    return request.param

def pytest_generate_tests(metafunc):
    """Dynamically set the params for operation_test_data."""
    if "operation_test_data" in metafunc.fixturenames:
        num_records = metafunc.config.getoption("num_records")
        metafunc.parametrize("operation_test_data", generate_test_cases(num_records), indirect=True)
