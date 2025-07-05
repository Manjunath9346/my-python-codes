class Solution:
    def isSumProperty(self, root):
        # If node is None or leaf node, it satisfies the property
        if root is None or (root.left is None and root.right is None):
            return 1
        
        # Get data of left and right children; 0 if child is None
        left_data = root.left.data if root.left else 0
        right_data = root.right.data if root.right else 0
        
        # Check current node value equals sum of children values
        if root.data == left_data + right_data:
            # Recursively check for left and right subtree
            return self.isSumProperty(root.left) and self.isSumProperty(root.right)
        else:
            return 0
print(isSumProperty(10))
