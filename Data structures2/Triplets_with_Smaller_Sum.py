class Solution:
    def countTriplets(self, n, target_sum, arr):
        """
        Count triplets with sum smaller than target using two-pointer approach after sorting.
        """
        arr.sort()
        count = 0
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                current_sum = arr[i] + arr[left] + arr[right]
                if current_sum < target_sum:
                    # All triplets between left and right are valid with i
                    count += right - left
                    left += 1
                else:
                    right -= 1
        return count

# Test cases
sol = Solution()

# Example 1
n1, sum1, arr1 = 4, 2, [-2, 0, 1, 3]
print(sol.countTriplets(n1, sum1, arr1))  # Output: 2

# Example 2
n2, sum2, arr2 = 5, 12, [5, 1, 3, 4, 7]
print(sol.countTriplets(n2, sum2, arr2))  # Output: 4

# Additional Test Case
n3, sum3, arr3 = 3, 5, [1, 2, 3]
print(sol.countTriplets(n3, sum3, arr3))  # Output: 0
