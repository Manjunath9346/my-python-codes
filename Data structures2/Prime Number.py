class Solution:
    def isPrime(self, n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        
        return True
obj = Solution()

print(obj.isPrime(7))    # True
print(obj.isPrime(25))   # False
print(obj.isPrime(1))    # False
print(obj.isPrime(2))    # True
print(obj.isPrime(97))   # True
print(obj.isPrime(100))  # False
