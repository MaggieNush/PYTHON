def classify_numbers(numbers):
    return {
        "even": [num for num in numbers if num % 2 == 0],
        "odd": [num for num in numbers if num % 2 != 0],
        "sum": sum(numbers)
    }

# Example usage:
numbers = [1, 2, 3, 4, 5, 6]
print(classify_numbers(numbers))

