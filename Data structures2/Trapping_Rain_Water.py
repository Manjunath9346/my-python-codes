class Solution:
    def maxWater(self, arr):
        n = len(arr)
        left, right = 0, n - 1
        left_max, right_max = 0, 0
        water = 0
        
        while left <= right:
            if arr[left] <= arr[right]:
                if arr[left] >= left_max:
                    left_max = arr[left]
                else:
                    water += left_max - arr[left]
                left += 1
            else:
                if arr[right] >= right_max:
                    right_max = arr[right]
                else:
                    water += right_max - arr[right]
                right -= 1
        
        return water
if __name__ == "__main__":
    obj = Solution()
    
    test_cases = [
        ([3, 0, 1, 0, 4, 0, 2], 10),
        ([3, 0, 2, 0, 4], 7),
        ([1, 2, 3, 4], 0),
        ([2, 1, 5, 3, 1, 0, 4], 9),
        ([0, 1, 0, 2, 1, 0, 3], 8)  # extra test case
    ]
    
    for arr, expected in test_cases:
        result = obj.maxWater(arr)
        print(f"Input: {arr} | Output: {result} | Expected: {expected} | {'PASS' if result == expected else 'FAIL'}")
