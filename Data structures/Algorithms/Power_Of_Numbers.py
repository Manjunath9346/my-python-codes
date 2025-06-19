class Solution:
    def reverse_exponentiation(self, n):
        # Helper to reverse the number
        def reverse(x):
            return int(str(x)[::-1])
        
        rev = reverse(n)
        return pow(n, rev)
sol = Solution()

# Test Case 1: Reverse is 1
print(sol.powerOfNumber(1))  # Expected: 1^1 = 1

# Test Case 2: Reverse is same as input
print(sol.powerOfNumber(11))  # Expected: 11^11 = 285311670611

# Test Case 3: Small number
print(sol.powerOfNumber(2))  # 2^2 = 4

# Test Case 4: n = 12 -> reverse = 21
print(sol.powerOfNumber(12))  # Expected: 12^21

# Test Case 5: n = 10 -> reverse = 1
print(sol.powerOfNumber(10))  # 10^1 = 10

# Test Case 6: Edge case large base
print(sol.powerOfNumber(123))  # 123^321 (a very large number)
