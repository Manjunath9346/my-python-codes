class Solution:
    def countAtMostK(self, arr, k):
        from collections import defaultdict

        n = len(arr)
        left = 0
        freq = defaultdict(int)
        count = 0

        for right in range(n):
            freq[arr[right]] += 1
            while len(freq) > k:
                freq[arr[left]] -= 1
                if freq[arr[left]] == 0:
                    del freq[arr[left]]
                left += 1
            count += right - left + 1

        return count
arr = [1, 2, 2, 3]
k = 2
arr = [1, 1, 1]
k = 1
