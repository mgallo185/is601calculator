"""REPL for the calculator application."""

from calculator.operation import Operation
from calculator.calculate import Calculation  # Import Calculation class

def calculator_repl():
    """Runs a simple Read-Eval-Print Loop (REPL) for the calculator."""
    operations = {
        "1": ("Addition", Operation.add),
        "2": ("Subtraction", Operation.subtract),
        "3": ("Multiplication", Operation.multiply),
        "4": ("Division", Operation.divide),
        "5": ("Exit", None),
        "6": ("View History", None),
        "7": ("Clear History", None)
    }

    calculations = []  # Store past calculations

    while True:
        print("\nCalculator Menu:")
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")

        choice = input("Select an operation (1-7): ").strip()

        if choice == "5":
            print("Exiting calculator. Goodbye!")
            break
        elif choice == "6":
            print("\nCalculation History:")
            for calc in Calculation.get_history():
                print(calc)
            continue
        elif choice == "7":
            Calculation.clear_history()
            print("Calculation history cleared.")
            continue

        if choice not in operations:
            print("Invalid choice. Please select a number between 1 and 7.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            operation_name, operation_func = operations[choice]

            if choice == "4" and num2 == 0:
                print("Error: Cannot divide by zero.")
                continue

            result = operation_func(num1, num2)
            print(f"Result of {operation_name.lower()}: {result}")

            # Store the calculation
            calculations.append(Calculation(operation_name, num1, num2, result))

        except ValueError:
            print("Error: Invalid input. Please enter numerical values.")

    # Print history before exiting
    print("\nPast Calculations:")
    for calc in calculations:
        print(calc)
