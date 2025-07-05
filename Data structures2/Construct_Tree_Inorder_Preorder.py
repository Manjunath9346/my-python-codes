# Definition for a binary tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, preorder):
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        self.pre_index = 0

        def construct(in_start, in_end):
            if in_start > in_end:
                return None

            root_val = preorder[self.pre_index]
            self.pre_index += 1
            root = Node(root_val)

            root_idx = inorder_map[root_val]

            root.left = construct(in_start, root_idx - 1)
            root.right = construct(root_idx + 1, in_end)

            return root

        return construct(0, len(inorder) - 1)

    def postorderTraversal(self, root, res):
        if root:
            self.postorderTraversal(root.left, res)
            self.postorderTraversal(root.right, res)
            res.append(root.data)
inorder = [3, 1, 4, 0, 2, 5]
preorder = [0, 1, 3, 4, 2, 5]
sol = Solution()
root = sol.buildTree(inorder, preorder)
result = []
sol.postorderTraversal(root, result)
print(result)  # Output: [3, 4, 1, 5, 2, 0]
