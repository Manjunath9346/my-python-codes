class Solution:
    def twoOddNum(self, arr):
        xor_all = 0
        for num in arr:
            xor_all ^= num
        
        # Get rightmost set bit
        set_bit = xor_all & -xor_all

        # Divide numbers into two groups based on the set_bit
        x = 0
        y = 0
        for num in arr:
            if num & set_bit:
                x ^= num
            else:
                y ^= num

        # Return in decreasing order
        return [max(x, y), min(x, y)]
obj = Solution()

print(obj.twoOddNum([4, 2, 4, 5, 2, 3, 3, 1]))  # ➤ [5, 1]
print(obj.twoOddNum([1, 7, 5, 7, 5, 4, 7, 4]))  # ➤ [7, 1]
print(obj.twoOddNum([10, 20, 10, 30, 20, 40]))  # ➤ [40, 30]
print(obj.twoOddNum([9, 7, 9, 11, 7, 13]))      # ➤ [13, 11]
