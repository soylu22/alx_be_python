# fns_and_dsa/arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations.

    Parameters:
        num1: The first number (float).
        num2: The second number (float).
        operation: The operation to perform - 'add', 'subtract', 'multiply', or 'divide'.

    Returns:
        float | str: The result of the operation, or an error message for invalid operations.
    """

    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"
