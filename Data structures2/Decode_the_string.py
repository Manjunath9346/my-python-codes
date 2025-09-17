class Solution:
    def decodedString(self, s: str) -> str:
        stack = []
        curr_num = 0
        curr_str = ""
        
        for ch in s:
            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)
            elif ch == "[":
                stack.append((curr_str, curr_num))
                curr_str, curr_num = "", 0
            elif ch == "]":
                last_str, num = stack.pop()
                curr_str = last_str + num * curr_str
            else:
                curr_str += ch
        
        return curr_str
sol = Solution()

print(sol.decodedString("3[b2[ca]]"))  
# Output: "bcacabcacabcaca"

print(sol.decodedString("3[ab]"))      
# Output: "ababab"

print(sol.decodedString("2[abc]3[cd]ef"))  
# Output: "abcabccdcdcdef"

print(sol.decodedString("10[a]"))      
# Output: "aaaaaaaaaa"
