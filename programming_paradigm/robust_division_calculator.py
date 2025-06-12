"""
Create two Python scripts: robust_division_calculator.py, which contains the division logic including error handling, and main.py, which interfaces with the user through the command line.
"""

def safe_divide(numerator, denominator):
    try:
        # Attempt to convert inputs to float
        num = float(numerator)
        den = float(denominator)
        
        # Attempt division
        result = num / den
        return f"The result of the division is {result}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Please enter numeric values only."
