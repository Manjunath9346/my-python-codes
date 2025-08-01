# User function Template for python3
class Solution:
    def kthElement(self, a, b, k):
        n, m = len(a), len(b)
        
        # Ensure a is the smaller array
        if n > m:
            return self.kthElement(b, a, k)

        low = max(0, k - m)
        high = min(k, n)

        while low <= high:
            cut1 = (low + high) // 2
            cut2 = k - cut1

            l1 = a[cut1 - 1] if cut1 > 0 else float('-inf')
            l2 = b[cut2 - 1] if cut2 > 0 else float('-inf')
            r1 = a[cut1] if cut1 < n else float('inf')
            r2 = b[cut2] if cut2 < m else float('inf')

            if l1 <= r2 and l2 <= r1:
                return max(l1, l2)
            elif l1 > r2:
                high = cut1 - 1
            else:
                low = cut1 + 1

        return -1
a = [2, 3, 6, 7, 9]
b = [1, 4, 8, 10]
k = 5

sol = Solution()
print(sol.kthElement(a, b, k))  # Output: 6
