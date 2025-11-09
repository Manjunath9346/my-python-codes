class Solution:
    def isProduct(self, arr, x):
        seen = set()

        for num in arr:
            # Avoid division by zero
            if num == 0:
                if x == 0:
                    return True
                continue

            # If x is divisible by num and x/num was seen earlier
            if x % num == 0 and (x // num) in seen:
                return True

            seen.add(num)

        return False
sol = Solution()

print(sol.isProduct([10, 20, 9, 40], 400))    #  Output: True  (10 * 40 = 400)
print(sol.isProduct([-10, 20, 9, -40], 30))   #  Output: False
print(sol.isProduct([2, 3, 5, 7], 15))        #  Output: True  (3 * 5 = 15)
print(sol.isProduct([0, 0, 2, 3], 0))         #  Output: True  (0 * 0 = 0)
print(sol.isProduct([1, 2, 3, 4], 10))        #  Output: False
