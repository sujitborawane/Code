def factorial(n):
    try:
        if n < 0:
            raise ValueError("Input must be a non-negative integer.")
        if n == 0 or n == 1:
            return 1
        else:
            result = 1
            for i in range(2, n + 1):
                result *= i
            return result
    except ValueError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"
try:
    num = int(input("Enter a non-negative integer to calculate its factorial: "))
    print(f"The factorial of {num} is {factorial(num)}")
except ValueError:
    print("Error: Please enter a valid integer.")
