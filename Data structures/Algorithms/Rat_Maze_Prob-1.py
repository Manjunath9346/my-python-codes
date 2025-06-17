class Solution:
    def ratInMaze(self, maze):
        n = len(maze)
        res = []

        def is_safe(x, y, visited):
            return 0 <= x < n and 0 <= y < n and maze[x][y] == 1 and not visited[x][y]

        def solve(x, y, path, visited):
            if x == n - 1 and y == n - 1:
                res.append(path)
                return

            visited[x][y] = True

            # Try all four directions in lexicographical order: D, L, R, U
            directions = [('D', 1, 0), ('L', 0, -1), ('R', 0, 1), ('U', -1, 0)]

            for dir_char, dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if is_safe(new_x, new_y, visited):
                    solve(new_x, new_y, path + dir_char, visited)

            visited[x][y] = False  # Backtrack

        if maze[0][0] == 1:
            visited = [[False] * n for _ in range(n)]
            solve(0, 0, "", visited)

        return sorted(res)
maze = [[1, 0, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 0, 0],
        [0, 1, 1, 1]]

sol = Solution()
print(sol.ratInMaze(maze))  # Output: ['DDRDRR', 'DRDDRR']
