# Square of numbers
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)

# Even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
evens = [x for x in numbers if x % 2 == 0]
print("Evens:", evens)

# Nested comprehension
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print("Matrix:", matrix)
