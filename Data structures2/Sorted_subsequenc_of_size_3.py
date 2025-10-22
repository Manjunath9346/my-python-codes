class Solution:
    def find3Numbers(self, arr):
        n = len(arr)
        if n < 3:
            return []

        smaller = [-1] * n
        greater = [-1] * n

        # Track the index of minimum element from the left
        min_index = 0
        for i in range(1, n):
            if arr[i] <= arr[min_index]:
                min_index = i
            else:
                smaller[i] = min_index

        # Track the index of maximum element from the right
        max_index = n - 1
        for i in range(n - 2, -1, -1):
            if arr[i] >= arr[max_index]:
                max_index = i
            else:
                greater[i] = max_index

        # Find a position j where both smaller[j] and greater[j] are valid
        for j in range(n):
            if smaller[j] != -1 and greater[j] != -1:
                return [arr[smaller[j]], arr[j], arr[greater[j]]]

        return []
print(Solution().find3Numbers([1, 2, 1, 1, 3]))   # [1, 2, 3]
print(Solution().find3Numbers([1, 1, 3]))         # []
print(Solution().find3Numbers([12, 11, 10, 5, 6, 2, 30]))  # [5, 6, 30]
print(Solution().find3Numbers([5, 4, 3, 2, 1]))   # []
