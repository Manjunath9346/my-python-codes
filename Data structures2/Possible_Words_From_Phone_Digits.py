class Solution:
    def possibleWords(self, arr):
        if not arr:
            return []
        
        keypad = {
            2: "abc", 3: "def", 4: "ghi", 5: "jkl",
            6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"
        }
        
        result = []
        
        def backtrack(index, path):
            if index == len(arr):
                if path:  # Only add non-empty combinations
                    result.append(path)
                return
            digit = arr[index]
            if digit in keypad:
                for char in keypad[digit]:
                    backtrack(index + 1, path + char)
            else:
                # If digit is 0 or 1, skip it and continue
                backtrack(index + 1, path)
        
        backtrack(0, "")
        return result


# Example Test Case
if __name__ == "__main__":
    sol = Solution()
    
    # Original failing test case
    print(sorted(sol.possibleWords([8, 8, 1])))
    # Output: ['tt', 'tu', 'tv', 'ut', 'uu', 'uv', 'vt', 'vu', 'vv']
