# Homework Assignment #3: "If" Statements
# This function checks for equality between any two of the three provided parameters.

def check_equality(param1, param2, param3):
    # Convert all parameters to integers if possible for comparison
    param1 = int(param1) if isinstance(param1, str) and param1.isdigit() else param1
    param2 = int(param2) if isinstance(param2, str) and param2.isdigit() else param2
    param3 = int(param3) if isinstance(param3, str) and param3.isdigit() else param3
    
    # Check for equality between any two parameters
    if param1 == param2 or param1 == param3 or param2 == param3:
        return True
    else:
        return False

# Example usage:
print(check_equality(6, 5, "5"))  # Output: True (Extra Credit Example)
print(check_equality(10, "10", 20))  # Output: True
print(check_equality(3, 4, 5))  # Output: False
print(check_equality("7", 7, 7))  # Output: True
