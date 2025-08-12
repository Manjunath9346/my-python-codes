class Solution:
    def totalElements(self, arr):
        from collections import defaultdict
        left = 0
        freq = defaultdict(int)
        max_len = 0
        
        for right in range(len(arr)):
            freq[arr[right]] += 1
            
            while len(freq) > 2:
                freq[arr[left]] -= 1
                if freq[arr[left]] == 0:
                    del freq[arr[left]]
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len
sol = Solution()
print(sol.totalElements([2, 1, 2]))           # Output: 3
print(sol.totalElements([3, 1, 2, 2, 2, 2]))  # Output: 5
print(sol.totalElements([1, 2, 3]))           # Output: 2
print(sol.totalElements([4, 4, 4, 4]))        # Output: 4
