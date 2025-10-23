class Solution:
    def isWordExist(self, mat, word):
        n, m = len(mat), len(mat[0])

        def dfs(i, j, k):
            if k == len(word):
                return True
            if i < 0 or i >= n or j < 0 or j >= m or mat[i][j] != word[k]:
                return False

            temp = mat[i][j]
            mat[i][j] = "#"  # mark as visited

            found = (dfs(i + 1, j, k + 1) or
                     dfs(i - 1, j, k + 1) or
                     dfs(i, j + 1, k + 1) or
                     dfs(i, j - 1, k + 1))

            mat[i][j] = temp  # unmark
            return found

        for i in range(n):
            for j in range(m):
                if mat[i][j] == word[0] and dfs(i, j, 0):
                    return True
        return False
sol = Solution()

# Test case 1
mat1 = [['T', 'E', 'E'], ['S', 'G', 'K'], ['T', 'E', 'L']]
word1 = "GEEK"
print(sol.isWordExist(mat1, word1))  #  True

# Test case 2
mat2 = [['T', 'E', 'U'], ['S', 'G', 'K'], ['T', 'E', 'L']]
word2 = "GEEK"
print(sol.isWordExist(mat2, word2))  #  False

# Test case 3
mat3 = [['A', 'B', 'A'], ['B', 'A', 'B']]
word3 = "AB"
print(sol.isWordExist(mat3, word3))  #  True

# Test case 4
mat4 = [['C', 'A', 'T'], ['A', 'T', 'C'], ['T', 'C', 'A']]
word4 = "CAT"
print(sol.isWordExist(mat4, word4))  #  True

# Test case 5
mat5 = [['A']]
word5 = "A"
print(sol.isWordExist(mat5, word5))  #  True

# Test case 6
mat6 = [['A']]
word6 = "B"
print(sol.isWordExist(mat6, word6))  #  False
