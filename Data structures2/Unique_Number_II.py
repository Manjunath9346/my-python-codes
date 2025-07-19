class Solution:
    def singleNum(self, arr):
        xor_all = 0
        for num in arr:
            xor_all ^= num

        # Get rightmost set bit
        diff_bit = xor_all & -xor_all

        x = 0
        y = 0
        for num in arr:
            if num & diff_bit:
                x ^= num
            else:
                y ^= num

        return sorted([x, y])
arr = [1, 2, 3, 2, 1, 4]
arr = [2, 1, 3, 2]
