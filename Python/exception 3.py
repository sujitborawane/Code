def dividenumbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division By Zero")
        result = None
    except ValueError:
        print("Error: Invalid Input Value")
        result = None
    except TypeError:
        print("Error: Invalid Data Type")
        result = None
    except Exception as e:
        print(f"An Unexpected error occurred: {e}")
        result = None
    finally:
        print("Exception Handling In Python")
        return result
result1 = dividenumbers(10,2)
print(result1)