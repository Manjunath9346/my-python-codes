class Solution:
    def reverseingroups(self, arr, k):
        n = len(arr)
        for i in range(0, n, k):
            arr[i:i+k] = arr[i:i+k][::-1]  # reverse current group
        return arr

# Test cases
sol = Solution()

# Test case 1
arr1 = [1, 2, 3, 4, 5]
k1 = 3
print(sol.reverseingroups(arr1, k1))  # Output: [3, 2, 1, 5, 4]

# Test case 2
arr2 = [5, 6, 8, 9]
k2 = 5
print(sol.reverseingroups(arr2, k2))  # Output: [9, 8, 6, 5]

# Test case 3 (k = 1, array remains same)
arr3 = [10, 20, 30]
k3 = 1
print(sol.reverseingroups(arr3, k3))  # Output: [10, 20, 30]
