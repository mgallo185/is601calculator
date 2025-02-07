"""REPL for the calculator application."""

from calculator.operation import Operation

def calculator_repl():
    """Runs a simple Read-Eval-Print Loop (REPL) for the calculator."""
    operations = {
        "1": ("Addition", Operation.add),
        "2": ("Subtraction", Operation.subtract),
        "3": ("Multiplication", Operation.multiply),
        "4": ("Division", Operation.divide),
        "5": ("Exit", None)
    }

    while True:
        print("\nCalculator Menu:")
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")

        choice = input("Select an operation (1-5): ").strip()

        if choice == "5":
            print("Exiting calculator. Goodbye!")
            break

        if choice not in operations:
            print("Invalid choice. Please select a number between 1 and 5.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            operation_name, operation_func = operations[choice]
            result = operation_func(num1, num2)
            print(f"Result of {operation_name.lower()}: {result}")

        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    calculator_repl()
