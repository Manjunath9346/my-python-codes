class Solution:
    def maxArea(self, mat):
        """
        Find the largest rectangle of 1s in a binary matrix using histogram + stack approach.
        """
        if not mat or not mat[0]:
            return 0
        
        n, m = len(mat), len(mat[0])
        
        # Function to find max area in histogram
        def maxHistArea(heights):
            stack = []
            max_area = 0
            i = 0
            while i < len(heights):
                if not stack or heights[stack[-1]] <= heights[i]:
                    stack.append(i)
                    i += 1
                else:
                    top = stack.pop()
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, heights[top] * width)
            while stack:
                top = stack.pop()
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, heights[top] * width)
            return max_area

        # Treat each row as histogram base
        heights = [0] * m
        max_rect = 0
        for i in range(n):
            for j in range(m):
                heights[j] = heights[j] + 1 if mat[i][j] == 1 else 0
            max_rect = max(max_rect, maxHistArea(heights))
        
        return max_rect

# Test cases
sol = Solution()

mat1 = [[0, 1, 1, 0],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 0, 0]]
print(sol.maxArea(mat1))  # Output: 8

mat2 = [[0, 1, 1],
        [1, 1, 1],
        [0, 1, 1]]
print(sol.maxArea(mat2))  # Output: 6

mat3 = [[1, 0, 1, 1, 1],
        [1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1]]
print(sol.maxArea(mat3))  # Output: 6
