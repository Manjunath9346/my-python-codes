from collections import defaultdict

class Solution:
    def findSubarray(self, arr):
        prefix_sum_count = defaultdict(int)
        prefix_sum = 0
        count = 0
        
        for num in arr:
            prefix_sum += num
            
            # If prefix sum is zero, it is a valid subarray
            if prefix_sum == 0:
                count += 1
            
            # If this prefix sum has been seen before, add its count
            if prefix_sum in prefix_sum_count:
                count += prefix_sum_count[prefix_sum]
            
            # Increase the frequency of the prefix sum
            prefix_sum_count[prefix_sum] += 1
        
        return count
if __name__ == "__main__":
    obj = Solution()
    
    test_cases = [
        ([0, 0, 5, 5, 0, 0], 6),
        ([6, -1, -3, 4, -2, 2, 4, 6, -12, -7], 4),
        ([0], 1),
        ([1, -1, 1, -1], 4)  # Extra case
    ]
    
    for arr, expected in test_cases:
        result = obj.findSubarray(arr)
        print(f"Input: {arr} | Output: {result} | Expected: {expected} | {'PASS' if result == expected else 'FAIL'}")
