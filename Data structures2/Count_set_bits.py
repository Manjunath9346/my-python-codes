class Solution:
    def countSetBits(self, n):
        count = 0
        i = 0
        
        while (1 << i) <= n:
            # Total pairs of 0 and 1 in ith bit
            total_pairs = (n + 1) // (1 << (i + 1))
            count += total_pairs * (1 << i)
            
            # If the remaining part after full pairs has extra 1s
            remainder = (n + 1) % (1 << (i + 1))
            if remainder > (1 << i):
                count += remainder - (1 << i)
            
            i += 1
        
        return count
# Test
ob = Solution()
print(ob.countSetBits(4))   # Output: 5
print(ob.countSetBits(17))  # Output: 35
print(ob.countSetBits(51))  # Output: 140
