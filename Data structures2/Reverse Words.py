class Solution:
    def reverseWords(self, s):
        # Split by dot and remove empty strings
        words = [w for w in s.split('.') if w]

        # Reverse the words
        words.reverse()

        # Join with single dots
        return '.'.join(words)
obj = Solution()

print(obj.reverseWords("i.like.this.program.very.much"))
# much.very.program.this.like.i

print(obj.reverseWords("..geeks..for.geeks."))
# geeks.for.geeks

print(obj.reverseWords("..home....."))
# home

print(obj.reverseWords("a.b..c"))
# c.b.a
