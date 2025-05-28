class Solution:
    def subarraySum(self, arr, target):
        n = len(arr)
        for i in range(n):
            cur_val = 0
            for j in range(i, n):
                cur_val += arr[j]
                if cur_val == target:
                    return [i+1, j+1]  # return as list, not tuple
                elif cur_val > target:
                    break
        return [-1]  # return [-1] if no such subarray exists
p = int(input("enter a number(target): "))
arr = [1, 2, 3, 7, 5]
sol = Solution()
result = sol.subarraySum(arr, p)
print(result)
