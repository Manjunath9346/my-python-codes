class Solution:
    def threeSumClosest(self, arr, target):
        arr.sort()
        n = len(arr)
        closest_sum = float('inf')

        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                curr_sum = arr[i] + arr[left] + arr[right]

                # Update closest if closer or same diff but larger sum
                if (abs(target - curr_sum) < abs(target - closest_sum)) or \
                   (abs(target - curr_sum) == abs(target - closest_sum) and curr_sum > closest_sum):
                    closest_sum = curr_sum

                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    return target  # Exact match found

        return closest_sum

obj = Solution()
print(obj.threeSumClosest([-7, 9, 8, 3, 1, 1], 2))     # ➤ 2
print(obj.threeSumClosest([5, 2, 7, 5], 13))           # ➤ 14
print(obj.threeSumClosest([1, 1, 1, 0], -100))         # ➤ 2
print(obj.threeSumClosest([0, 2, 1, -3], 1))           # ➤ 0
print(obj.threeSumClosest([10, 20, 30, 40, 50], 85))   # ➤ 90
