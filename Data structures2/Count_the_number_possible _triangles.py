class Solution:
    def countTriangles(self, arr):
        arr.sort()
        n = len(arr)
        count = 0
        
        for k in range(n - 1, 1, -1):  # Fix the largest side
            i, j = 0, k - 1
            while i < j:
                if arr[i] + arr[j] > arr[k]:
                    count += (j - i)  # All elements between i and j form triangles
                    j -= 1
                else:
                    i += 1
        return count
if __name__ == "__main__":
    obj = Solution()
    
    test_cases = [
        ([4, 6, 3, 7], 3),
        ([10, 21, 22, 100, 101, 200, 300], 6),
        ([1, 2, 3], 0),
        ([2, 2, 3, 4], 3)  # Extra test case
    ]
    
    for arr, expected in test_cases:
        result = obj.countTriangles(arr)
        print(f"Input: {arr} | Output: {result} | Expected: {expected} | {'PASS' if result == expected else 'FAIL'}")
