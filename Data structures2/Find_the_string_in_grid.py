class Solution:
    # Function to search the word in grid in all 8 directions
    def searchWord(self, grid, word):
        n, m = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                      (-1, -1), (-1, 1), (1, -1), (1, 1)]

        def is_valid(i, j):
            return 0 <= i < n and 0 <= j < m

        def check(i, j):
            if grid[i][j] != word[0]:
                return False
            for dx, dy in directions:
                x, y, k = i, j, 0
                while k < len(word) and is_valid(x, y) and grid[x][y] == word[k]:
                    x += dx
                    y += dy
                    k += 1
                if k == len(word):
                    return True
            return False

        result = []
        for i in range(n):
            for j in range(m):
                if check(i, j):
                    result.append([i, j])
        return result
# Test Case 1
grid = [['a','b','c'],
        ['d','r','f'],
        ['g','h','i']]
word = "abc"
print(Solution().searchWord(grid, word))  
# Expected Output: [[0, 0]]

# Test Case 2
grid = [['a','b','a','b'],
        ['a','b','e','b'],
        ['e','b','e','b']]
word = "abe"
print(Solution().searchWord(grid, word))  
# Expected Output: [[0,0],[0,2],[1,0]]

# Test Case 3
grid = [['x','y','z'],
        ['a','b','c'],
        ['d','e','f']]
word = "xyz"
print(Solution().searchWord(grid, word))  
# Expected Output: [[0,0]]

# Test Case 4 (No match)
grid = [['a','b'], ['c','d']]
word = "xyz"
print(Solution().searchWord(grid, word))  
# Expected Output: []

# Test Case 5 (Diagonal case)
grid = [['a','b','c'],
        ['d','a','b'],
        ['e','d','a']]
word = "ada"
print(Solution().searchWord(grid, word))  
# Expected Output: [[0,0]]
