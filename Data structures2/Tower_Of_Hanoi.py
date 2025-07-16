class Solution:
    def towerOfHanoi(self, n, fromm, to, aux):
        self.moves = []

        def solve(n, fromm, to, aux):
            if n == 0:
                return
            solve(n - 1, fromm, aux, to)
            self.moves.append(f"move disk {n} from rod {fromm} to rod {to}")
            solve(n - 1, aux, to, fromm)

        solve(n, fromm, to, aux)
        return len(self.moves)
sol = Solution()
print(sol.towerOfHanoi(2, 1, 3, 2))  # Output: 3
print(sol.towerOfHanoi(3, 1, 3, 2))  # Output: 7
print(sol.towerOfHanoi(0, 1, 3, 2))  # Output: 0
