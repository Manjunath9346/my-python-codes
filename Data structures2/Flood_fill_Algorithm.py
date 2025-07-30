class Solution:
    def floodFill(self, image, sr, sc, newColor):
        rows, cols = len(image), len(image[0])
        oldColor = image[sr][sc]
        
        # If the starting pixel already has the new color, no need to change
        if oldColor == newColor:
            return image
        
        def dfs(r, c):
            # Boundary check and same color check
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != oldColor:
                return
            
            # Change the color
            image[r][c] = newColor
            
            # Explore 4 directions
            dfs(r+1, c)  # Down
            dfs(r-1, c)  # Up
            dfs(r, c+1)  # Right
            dfs(r, c-1)  # Left
        
        dfs(sr, sc)
        return image
if __name__ == "__main__":
    obj = Solution()
    
    # Test Case 1
    image = [[1, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]
    sr, sc, newColor = 1, 2, 2
    print(obj.floodFill(image, sr, sc, newColor))
    # Expected: [[2, 2, 2, 0], [0, 2, 2, 2], [1, 0, 2, 2]]
    
    # Test Case 2
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr, sc, newColor = 1, 1, 2
    print(obj.floodFill(image, sr, sc, newColor))
    # Expected: [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    
    # Test Case 3
    image = [[0, 1, 0], [0, 1, 0]]
    sr, sc, newColor = 0, 1, 0
    print(obj.floodFill(image, sr, sc, newColor))
    # Expected: [[0, 0, 0], [0, 0, 0]]
