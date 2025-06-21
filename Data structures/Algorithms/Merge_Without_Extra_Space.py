class Solution:
    def mergeArrays(self, a, b):
        n = len(a)
        m = len(b)
        i, j = n - 1, 0

        # Swap largest elements of a with smallest of b if a[i] > b[j]
        while i >= 0 and j < m:
            if a[i] > b[j]:
                a[i], b[j] = b[j], a[i]
            i -= 1
            j += 1

        # Re-sort both arrays
        a.sort()
        b.sort()

        return a, b
a = [1, 5, 9, 10, 15, 20]
b = [2, 3, 8, 13]

sol = Solution()
a, b = sol.mergeArrays(a, b)
print(" ".join(map(str, a)))
print(" ".join(map(str, b)))
