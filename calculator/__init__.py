from calculator.operation import Operation

def run_calculator():
    """Runs the REPL for the calculator."""
    print("Welcome to the calculator!")
    print("Supported operations: add, subtract, multiply, divide")
    print("Type 'exit' to quit.")

    while True:
        # Get user input
        operation = input("Enter operation (add, subtract, multiply, divide): ").lower()

        if operation == 'exit':
            print("Exiting the calculator. Goodbye!")
            break

        # Validate operation
        if operation not in ['add', 'subtract', 'multiply', 'divide']:
            print("Invalid operation. Please try again.")
            continue

        try:
            # Get operands
            a = float(input("Enter the first operand: "))
            b = float(input("Enter the second operand: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        try:
            # Perform the operation using the static methods from the Operation class
            if operation == 'add':
                result = Operation.add(a, b)
            elif operation == 'subtract':
                result = Operation.subtract(a, b)
            elif operation == 'multiply':
                result = Operation.multiply(a, b)
            elif operation == 'divide':
                result = Operation.divide(a, b)

            # Display the result
            print(f"The result of {operation}({a}, {b}) is: {result}")

        except ValueError as e:
            # Handle division by zero or any other value-related errors
            print(f"Error: {e}")
