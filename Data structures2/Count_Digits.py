class Solution:
    def evenlyDivides(self, n):
        original = n
        count = 0
        
        while n > 0:
            digit = n % 10
            n = n // 10

            if digit != 0 and original % digit == 0:
                count += 1

        return count
obj = Solution()

print(obj.evenlyDivides(12))    # Expected 2   (1, 2)
print(obj.evenlyDivides(2446))  # Expected 1   (only 2)
print(obj.evenlyDivides(23))    # Expected 0
print(obj.evenlyDivides(1012))  # Expected 3   (1,1,2)
