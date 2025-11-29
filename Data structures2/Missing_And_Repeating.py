class Solution:
    def findTwoElement(self, arr):
        n = len(arr)

        # Expected sums
        sum_n = n * (n + 1) // 2
        sum_sq_n = n * (n + 1) * (2 * n + 1) // 6

        # Actual sums
        sum_arr = 0
        sum_sq_arr = 0

        for x in arr:
            sum_arr += x
            sum_sq_arr += x * x

        # Let repeating = R, missing = M

        # 1) M - R = sum_n - sum_arr
        diff = sum_n - sum_arr

        # 2) M^2 - R^2 = sum_sq_n - sum_sq_arr = (M - R)(M + R)
        sq_diff = sum_sq_n - sum_sq_arr

        # (M + R) = sq_diff / diff
        sum_val = sq_diff // diff

        # Solve:
        M = (diff + sum_val) // 2
        R = sum_val - M

        return [R, M]
obj = Solution()

print(obj.findTwoElement([2, 2]))                     # Expected: [2, 1]
print(obj.findTwoElement([1, 3, 3]))                  # Expected: [3, 2]
print(obj.findTwoElement([4, 3, 6, 2, 1, 1]))         # Expected: [1, 5]
print(obj.findTwoElement([1, 1]))                     # Expected: [1, 2]
print(obj.findTwoElement([3, 1, 3]))                  # Expected: [3, 2]
