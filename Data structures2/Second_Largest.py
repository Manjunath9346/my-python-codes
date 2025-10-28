class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        first = -1
        second = -1
        for i in arr:
            if i > first:
               second = first
               first = i
            elif i > second and i < first:
               second = i
        return second
obj = Solution()
print(obj.getSecondLargest([12, 35, 1, 10, 34, 1]))  # 34
print(obj.getSecondLargest([10, 5, 10]))             # 5
print(obj.getSecondLargest([10, 10, 10]))            # -1
