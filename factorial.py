# Function to calculate factorial using recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Test the factorial function with some example inputs
if __name__ == "__main__":
    print(factorial(5))  # Output: 120
    print(factorial(0))  # Output: 1
    print(factorial(3))  # Output: 6