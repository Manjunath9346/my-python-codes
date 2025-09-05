class Solution:
    def largestPrimeFactor(self, n):
        max_prime = -1
        
        # Remove factors of 2
        while n % 2 == 0:
            max_prime = 2
            n //= 2
        
        # Check for odd factors from 3 onwards
        i = 3
        while i * i <= n:
            while n % i == 0:
                max_prime = i
                n //= i
            i += 2
        
        # If n is a prime number greater than 2
        if n > 2:
            max_prime = n
        
        return max_prime

# Test Cases
sol = Solution()
print(sol.largestPrimeFactor(5))      # Output: 5
print(sol.largestPrimeFactor(24))     # Output: 3
print(sol.largestPrimeFactor(13195))  # Output: 29
print(sol.largestPrimeFactor(100))    # Output: 5
print(sol.largestPrimeFactor(2))      # Output: 2
