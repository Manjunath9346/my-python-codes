class Solution:
    def pythagoreanTriplet(self, arr):
        squares = set([x * x for x in arr])
        n = len(arr)

        for i in range(n):
            for j in range(i + 1, n):
                if arr[i]*arr[i] + arr[j]*arr[j] in squares:
                    return True
        return False
sol = Solution()

print(sol.pythagoreanTriplet([3, 2, 4, 6, 5]))  # Output: True
print(sol.pythagoreanTriplet([3, 8, 5]))        # Output: False
print(sol.pythagoreanTriplet([1, 1, 1]))        # Output: False
print(sol.pythagoreanTriplet([9, 40, 41]))      # Output: True
