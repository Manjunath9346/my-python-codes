# List Operations  Sum, Max, Reverse

def list_operations(numbers):
    print("List:", numbers)
    print("Sum:", sum(numbers))
    print("Maximum:", max(numbers))
    print("Reversed:", list(reversed(numbers)))


nums = list(map(int, input("Enter numbers separated by space: ").split()))
list_operations(nums)
