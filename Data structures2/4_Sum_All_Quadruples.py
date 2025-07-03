class Solution:
    def fourSum(self, arr, target):
        arr.sort()
        n = len(arr)
        result = []

        for i in range(n):
            if i > 0 and arr[i] == arr[i - 1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and arr[j] == arr[j - 1]:
                    continue
                left, right = j + 1, n - 1
                while left < right:
                    total = arr[i] + arr[j] + arr[left] + arr[right]
                    if total == target:
                        result.append([arr[i], arr[j], arr[left], arr[right]])
                        while left < right and arr[left] == arr[left + 1]:
                            left += 1
                        while left < right and arr[right] == arr[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return result
sol = Solution()

print(sol.fourSum([0, 0, 2, 1, 1], 3))        # Output: [[0, 0, 1, 2]]
print(sol.fourSum([10, 2, 3, 4, 5, 7, 8], 23))# Output: [[2, 3, 8, 10], [2, 4, 7, 10], [3, 5, 7, 8]]
print(sol.fourSum([0, 0, 2, 1, 1], 2))        # Output: [[0, 0, 1, 1]]
print(sol.fourSum([1, 0, -1, 0, -2, 2], 0))   # Output: [[-2, -1, 1, 2], [-2,  0, 0, 2], [-1,  0, 0, 1]]
