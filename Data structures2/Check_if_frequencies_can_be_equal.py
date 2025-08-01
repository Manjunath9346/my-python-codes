from collections import Counter

class Solution:
    def sameFreq(self, s: str) -> bool:
        freq = Counter(s)
        freq_values = list(freq.values())
        
        # Case 1: Already equal
        if len(set(freq_values)) == 1:
            return True
        
        # Try removing one occurrence from each character and check
        for char in freq:
            freq[char] -= 1
            if freq[char] == 0:
                del freq[char]
            values = list(freq.values())
            if len(set(values)) == 1:
                return True
            # restore
            freq[char] = freq.get(char, 0) + 1
        
        return False
if __name__ == "__main__":
    obj = Solution()
    
    test_cases = [
        ("xyyz", True),
        ("xyyzz", True),
        ("xxxxyyzz", False),
        ("aabbcc", True),  # Already equal
        ("aabbccc", True), # Remove one 'c'
        ("abc", True)      # Already equal
    ]
    
    for s, expected in test_cases:
        result = obj.sameFreq(s)
        print(f"Input: '{s}' | Output: {result} | Expected: {expected} | {'PASS' if result == expected else 'FAIL'}")
