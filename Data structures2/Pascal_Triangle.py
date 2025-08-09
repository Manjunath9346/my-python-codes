class Solution:
    def nthRowOfPascalTriangle(self, n):
        row = [1]
        for i in range(1, n):
            row.append(row[i-1] * (n - i) // i)
        return row
sol = Solution()

print(sol.nthRowOfPascalTriangle(4))  # Output: [1, 3, 3, 1]
print(sol.nthRowOfPascalTriangle(5))  # Output: [1, 4, 6, 4, 1]
print(sol.nthRowOfPascalTriangle(1))  # Output: [1]
print(sol.nthRowOfPascalTriangle(6))  # Output: [1, 5, 10, 10, 5, 1]
print(sol.nthRowOfPascalTriangle(3))  # Output: [1, 2, 1]
