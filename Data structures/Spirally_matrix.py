class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, mat):
        result = []
        if not mat:
            return result

        top, bottom = 0, len(mat) - 1
        left, right = 0, len(mat[0]) - 1

        while top <= bottom and left <= right:
            # Traverse from Left to Right
            for i in range(left, right + 1):
                result.append(mat[top][i])
            top += 1

            # Traverse from Top to Bottom
            for i in range(top, bottom + 1):
                result.append(mat[i][right])
            right -= 1

            # Traverse from Right to Left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(mat[bottom][i])
                bottom -= 1

            # Traverse from Bottom to Top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(mat[i][left])
                left += 1

        return result
mat = [
    [1, 2, 3, 4], 
    [5, 6, 7, 8], 
    [9, 10, 11, 12], 
    [13, 14, 15, 16]
]

sol = Solution()
print(sol.spirallyTraverse(mat))
