class Solution:

    # Function to return a list containing the union of the two arrays.
    def findUnion(self, a, b):
        n, m = len(a), len(b)
        i, j = 0, 0
        result = []
        
        while i < n and j < m:
            # Skip duplicates in 'a'
            while i > 0 and i < n and a[i] == a[i - 1]:
                i += 1
            # Skip duplicates in 'b'
            while j > 0 and j < m and b[j] == b[j - 1]:
                j += 1
            if i >= n or j >= m:
                break

            if a[i] < b[j]:
                result.append(a[i])
                i += 1
            elif a[i] > b[j]:
                result.append(b[j])
                j += 1
            else:
                result.append(a[i])
                i += 1
                j += 1

        # Add remaining elements in 'a'
        while i < n:
            if i == 0 or a[i] != a[i - 1]:
                result.append(a[i])
            i += 1

        # Add remaining elements in 'b'
        while j < m:
            if j == 0 or b[j] != b[j - 1]:
                result.append(b[j])
            j += 1

        return result
sol = Solution()
a = [2, 2, 3, 4, 5]
b = [1, 1, 2, 3, 4]
print(sol.findUnion(a, b))  # Output: [1, 2, 3, 4, 5]
