class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder, postorder):
        # Build a hashmap for inorder indices to access root positions quickly
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        self.post_idx = len(postorder) - 1  # start from last element in postorder

        def build(left, right):
            # Base case
            if left > right:
                return None
            
            # Pick current root from postorder
            root_val = postorder[self.post_idx]
            self.post_idx -= 1
            root = Node(root_val)
            
            # Build right subtree first (because postorder -> left, right, root)
            root_idx = idx_map[root_val]
            root.right = build(root_idx + 1, right)
            root.left = build(left, root_idx - 1)
            
            return root
        
        return build(0, len(inorder) - 1)
# Helper function to print preorder traversal (to verify tree)
def preorder(root):
    return [] if not root else [root.data] + preorder(root.left) + preorder(root.right)

# Example 1
sol = Solution()
inorder = [4, 8, 2, 5, 1, 6, 3, 7]
postorder = [8, 4, 5, 2, 6, 7, 3, 1]
root = sol.buildTree(inorder, postorder)
print(preorder(root))  # Expected preorder: [1, 2, 4, 8, 5, 3, 6, 7]

# Example 2
inorder = [9, 5, 2, 3, 4]
postorder = [5, 9, 3, 4, 2]
root = sol.buildTree(inorder, postorder)
print(preorder(root))  # Expected preorder: [2, 9, 5, 4, 3]
