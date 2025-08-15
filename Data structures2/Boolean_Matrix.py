class Solution:
    def booleanMatrix(self, mat):
        r, c = set(), set()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]: r.add(i); c.add(j)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] = 1 if i in r or j in c else 0
        return mat  # optional, just to see output
s = Solution()

# Test case 1
print(s.booleanMatrix([[1, 0], [0, 0]]))  # Output: [[1, 1], [1, 0]]

# Test case 2
print(s.booleanMatrix([[1, 0, 0], [1, 0, 0], [1, 0, 0], [0, 0, 0]]))  # Output: [[1,1,1],[1,1,1],[1,1,1],[1,0,0]]

# Test case 3
print(s.booleanMatrix([[0, 0], [0, 0]]))  # Output: [[0,0],[0,0]]
