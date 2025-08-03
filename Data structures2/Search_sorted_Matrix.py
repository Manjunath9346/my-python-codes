class Solution:
    def searchMatrix(self, mat, x):
        n = len(mat)
        m = len(mat[0])
        
        low, high = 0, n * m - 1
        
        while low <= high:
            mid = (low + high) // 2
            row = mid // m
            col = mid % m
            
            if mat[row][col] == x:
                return True
            elif mat[row][col] < x:
                low = mid + 1
            else:
                high = mid - 1
        
        return False
if __name__ == "__main__":
    obj = Solution()
    
    test_cases = [
        ([[1, 5, 9], [14, 20, 21], [30, 34, 43]], 14, True),
        ([[1, 5, 9, 11], [14, 20, 21, 26], [30, 34, 43, 50]], 42, False),
        ([[87, 96, 99], [101, 103, 111]], 101, True),
        ([[1]], 1, True),
        ([[1]], 2, False)
    ]
    
    for mat, x, expected in test_cases:
        result = obj.searchMatrix(mat, x)
        print(f"Matrix: {mat}, x={x} | Output: {result} | Expected: {expected} | {'PASS' if result == expected else 'FAIL'}")
