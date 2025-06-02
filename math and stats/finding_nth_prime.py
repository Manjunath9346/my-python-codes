# Function to check if a number is prime
def isPrime(n):
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

# Function to find the nth prime
def nThprime(n):
    if n == 1:
        return 2
    nprimes, i = 1, 3  # 2 is already counted as the 1st prime
    while True:
        if isPrime(i):
            nprimes += 1
            if nprimes == n:
                return i
        i += 2  # increment by 2 to skip even numbers

# Print the first 10 prime numbers
for i in range(1, 11):
    print(f"{i}th prime = {nThprime(i)}")
