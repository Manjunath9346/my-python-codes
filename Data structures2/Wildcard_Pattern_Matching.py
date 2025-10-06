class Solution:
    def wildCard(self, txt, pat):
        n, m = len(txt), len(pat)
        i = j = 0
        star_idx = -1
        match = 0
        
        while i < n:
            if j < m and (pat[j] == txt[i] or pat[j] == '?'):
                i += 1
                j += 1
            elif j < m and pat[j] == '*':
                star_idx = j
                match = i
                j += 1
            elif star_idx != -1:
                # Backtrack: '*' matches one more character
                j = star_idx + 1
                match += 1
                i = match
            else:
                return False
        
        # Check remaining pattern characters
        while j < m and pat[j] == '*':
            j += 1
        
        return j == m


# Example Test Cases
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.wildCard("abcde", "a?c*"))       # True
    print(sol.wildCard("baaabab", "a*ab"))     # False
    print(sol.wildCard("abc", "*"))            # True
    print(sol.wildCard("abcd", "a*d"))         # True
    print(sol.wildCard("abcd", "a*c?"))        # True
