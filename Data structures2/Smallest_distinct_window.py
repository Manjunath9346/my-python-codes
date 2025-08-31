class Solution:
    def findSubString(self, s):
        unique_chars = set(s)   # all unique characters in string
        n = len(s)
        required = len(unique_chars)
        
        freq = {}
        left = 0
        count = 0
        min_len = n + 1
        
        for right in range(n):
            freq[s[right]] = freq.get(s[right], 0) + 1
            if len(freq) == required:   # all unique chars present
                # shrink window from left
                while left <= right and len(freq) == required:
                    min_len = min(min_len, right - left + 1)
                    freq[s[left]] -= 1
                    if freq[s[left]] == 0:
                        del freq[s[left]]
                    left += 1
        return min_len
if __name__ == "__main__":
    obj = Solution()
    print(obj.findSubString("aabcbcdbca"))     # Expected: 4 ("dbca")
    print(obj.findSubString("aaab"))           # Expected: 2 ("ab")
    print(obj.findSubString("geeksforgeeks"))  # Expected: 7 ("eksforg"/"ksforge")
    print(obj.findSubString("aaaa"))           # Expected: 1 ("a")
    print(obj.findSubString("abc"))            # Expected: 3 ("abc")
