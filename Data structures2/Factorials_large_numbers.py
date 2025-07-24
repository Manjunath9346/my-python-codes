class Solution:
    def factorial(self, n):
        result = [1]  # Start with 1 as the initial factorial value
        for i in range(2, n + 1):
            carry = 0
            for j in range(len(result)):
                temp = result[j] * i + carry
                result[j] = temp % 10
                carry = temp // 10
            while carry:
                result.append(carry % 10)
                carry //= 10
        return result[::-1]  # Reverse to get most significant digit first
sol = Solution()

# Test Case 1
print(sol.factorial(5))     # Output: [1, 2, 0]

# Test Case 2
print(sol.factorial(10))    # Output: [3, 6, 2, 8, 8, 0, 0]

# Test Case 3
print(sol.factorial(1))     # Output: [1]

# Test Case 4
print(sol.factorial(20))    # Output: [2, 4, 3, 2, 9, 0, 2, 3, 7, 5, 2, 0, 8, 0, 0, 0]

# Test Case 5
print(sol.factorial(100))   # Output: [9, 3, 3, 2, ..., 0, 0, 0] (158 digits)
