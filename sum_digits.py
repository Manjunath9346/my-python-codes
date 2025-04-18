#  Sum of Digits

def sum_of_digits(number):
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number = number // 10
    return total

# Example usage
num = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(num))
