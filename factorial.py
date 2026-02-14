def factorial(n):
    """
    Calculate the factorial of a non-negative integer.
    The factorial of n (denoted as n!) is the product of all positive integers 
    less than or equal to n. By definition, 0! = 1 and 1! = 1.
    Args:
        n (int): A non-negative integer for which to calculate the factorial.
    Returns:
        int: The factorial of n.
    Raises:
        ValueError: If n is a negative number, as factorial is not defined 
                   for negative integers.
    Examples:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
        >>> factorial(1)
        1
    """
    """Calculate the factorial of a number."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# Example usage
if __name__ == "__main__":
    print(factorial(5))  # Output: 120
    print(factorial(0))  # Output: 1