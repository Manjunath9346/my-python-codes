class Solution:
    def Sorted(self, s):
        if s:
            temp = s.pop()
            self.Sorted(s)
            self.insert_sorted(s, temp)

    def insert_sorted(self, s, element):
        if not s or s[-1] <= element:
            s.append(element)
        else:
            temp = s.pop()
            self.insert_sorted(s, element)
            s.append(temp)
s = [3, 2, 1]
Solution().Sorted(s)
print(s[::-1])  # Output: [3, 2, 1]
s = [11, 2, 32, 3, 41]
Solution().Sorted(s)
print(s[::-1])  # Output: [41, 32, 11, 3, 2]
