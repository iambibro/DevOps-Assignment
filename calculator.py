def add(a, b):
    if a < 0 or b < 0:
        raise ValueError("Both numbers should be positive ")
    return a + b

def subtract(a, b):
    if a < 0 or b < 0:
        raise ValueError("Both numbers should be positive")
    return a - b

def multiply(a, b):
    if a < 0 or b < 0:
        raise ValueError("Both numbers should be positive")
    return a * b
