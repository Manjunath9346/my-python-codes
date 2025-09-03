# User function Template for python3
class Solution:
    def maximumPath(self, mat):
        n, m = len(mat), len(mat[0])

        # Start from 2nd last row and move upward
        for i in range(n - 2, -1, -1):
            for j in range(m):
                # Pick max from directly below, left-diagonal, and right-diagonal
                down = mat[i + 1][j]
                left = mat[i + 1][j - 1] if j - 1 >= 0 else 0
                right = mat[i + 1][j + 1] if j + 1 < m else 0
                mat[i][j] += max(down, left, right)

        # Max path sum will be the max in the first row
        return max(mat[0])
obj = Solution()

print(obj.maximumPath([[3, 6, 1], [2, 3, 4], [5, 5, 1]]))   # Output: 15
print(obj.maximumPath([[2, 1, 1], [1, 2, 2]]))              # Output: 4
print(obj.maximumPath([[25]]))                              # Output: 25
print(obj.maximumPath([[10, 20, 30], [5, 50, 5], [10, 5, 100]]))  # Output: 180
