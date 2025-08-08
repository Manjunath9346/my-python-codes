class Solution:
    def canPair(self, arr, k):
        freq = [0]*k
        for num in arr:
            freq[num % k] += 1
        if freq[0] % 2 != 0:
            return False
        for i in range(1, k//2 + 1):
            if i != k - i:
                if freq[i] != freq[k - i]:
                    return False
            else:
                if freq[i] % 2 != 0:
                    return False
        return True
sol = Solution()

# Test case 1: True, pairs: (9,3), (5,7)
print(sol.canPair([9, 5, 7, 3], 6))  # Output: True

# Test case 2: False, can't pair all elements
print(sol.canPair([4, 4, 4], 4))  # Output: False

# Test case 3: True, single pair (4,4)
print(sol.canPair([4, 4], 4))  # Output: True

# Additional test cases
print(sol.canPair([2, 2, 1, 7, 5, 3], 4))  # True
print(sol.canPair([1, 2, 3, 4, 5, 10, 6, 7, 8, 9], 5))  # True
print(sol.canPair([1, 2, 3, 4, 5], 10))  # False
