class Solution:
    def isSubset(self, a, b):
        # frequency map for array a
        freq = {}

        for x in a:
            freq[x] = freq.get(x, 0) + 1

        # check all elements in b
        for x in b:
            if x not in freq or freq[x] == 0:
                return False
            freq[x] -= 1   # use one occurrence

        return True
obj = Solution()

print(obj.isSubset([11, 7, 1, 13, 21, 3, 7, 3], [11, 3, 7, 1, 7]))  
# Expected: True

print(obj.isSubset([1, 2, 3, 4, 4, 5, 6], [1, 2, 4]))  
# Expected: True

print(obj.isSubset([10, 5, 2, 23, 19], [19, 5, 3]))  
# Expected: False

print(obj.isSubset([1, 1, 2, 2], [1, 1, 2]))  
# Expected: True

print(obj.isSubset([1, 2, 3], [1, 1]))  
# Expected: False
