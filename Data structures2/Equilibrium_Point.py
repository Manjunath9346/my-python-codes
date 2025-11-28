class Solution:
    # Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        total_sum = sum(arr)
        left_sum = 0

        for i in range(len(arr)):
            # right sum = total_sum - left_sum - arr[i]
            if left_sum == total_sum - left_sum - arr[i]:
                return i
            left_sum += arr[i]

        return -1
obj = Solution()

print(obj.findEquilibrium([1, 2, 0, 3]))        # Expected: 2
print(obj.findEquilibrium([1, 1, 1, 1]))        # Expected: -1
print(obj.findEquilibrium([-7, 1, 5, 2, -4, 3, 0]))  # Expected: 3
print(obj.findEquilibrium([0, 0, 0]))           # Expected: 0
print(obj.findEquilibrium([2, -2, 0, 2, -2]))   # Expected: 2
print(obj.findEquilibrium([1, -1, 4]))          # Expected: 2
print(obj.findEquilibrium([3, -1, -2]))         # Expected: 0
