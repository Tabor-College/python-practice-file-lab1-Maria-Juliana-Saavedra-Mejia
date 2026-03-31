# app.py - Complete Application Code

def add(a, b):
    """Add two numbers together."""
    return a + b


def divide(a, b):
    """Divide with error handling."""
    if b == 0:
        return "Error"
    return a / b


def divide_strict(a, b):
    """Divide with proper exception handling."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def is_even(n):
    """Check if a number is even."""
    return n % 2 == 0