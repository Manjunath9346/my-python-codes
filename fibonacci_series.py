#   Fibonacci Series up to N Terms

def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

# Example usage
terms = int(input("Enter the number of terms: "))
print("Fibonacci series:")
print(fibonacci(terms))
