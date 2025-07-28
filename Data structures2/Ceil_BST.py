class Solution:
    def findCeil(self, root, inp):
        ceil = -1
        while root:
            if root.key == inp:
                return root.key
            elif root.key < inp:
                root = root.right
            else:
                ceil = root.key
                root = root.left
        return ceil
# Tree: [5, 1, 7, None, 2, None, None, None, 3]

sol = Solution()
print(sol.findCeil(root, 3))  # Output: 3
# Tree: [10, 5, 11, 4, 7, None, None, None, None, None, 8]

sol = Solution()
print(sol.findCeil(root, 6))  # Output: 7
