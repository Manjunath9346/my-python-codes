class Solution:
    def twoSum(self, arr, target):
        seen = set()

        for num in arr:
            complement = target - num
            if complement in seen:
                return True    # pair found
            seen.add(num)

        return False    # no pair
obj = Solution()

print(obj.twoSum([0, -1, 2, -3, 1], -2))  
# Expected: True  (-3 + 1)

print(obj.twoSum([1, -2, 1, 0, 5], 0))  
# Expected: False

print(obj.twoSum([11], 11))  
# Expected: False  (no pair possible)

print(obj.twoSum([2, 7, 11, 15], 9))  
# Expected: True  (2 + 7)

print(obj.twoSum([-5, -3, -1, 2, 4], -4))  
# Expected: True  (-5 + 1 or -3 + -1)
