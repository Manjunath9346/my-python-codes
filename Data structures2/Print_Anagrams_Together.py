from collections import defaultdict

class Solution:
    def anagrams(self, arr):
        groups = defaultdict(list)
        
        for word in arr:
            # use sorted word as key
            key = ''.join(sorted(word))
            groups[key].append(word)
        
        # return values in order of first appearance
        return list(groups.values())
s = Solution()
print(s.anagrams(["act", "god", "cat", "dog", "tac"]))
# Output: [["act", "cat", "tac"], ["god", "dog"]]
