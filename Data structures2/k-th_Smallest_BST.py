class Solution:
    def kthSmallest(self, root, k):
        self.count = 0
        self.result = -1
        
        def inorder(node):
            if not node or self.result != -1:
                return
            inorder(node.left)
            self.count += 1
            if self.count == k:
                self.result = node.data
                return
            inorder(node.right)
        
        inorder(root)
        return self.result
# Helper function to build BST from list (level order)
from collections import deque
def build_tree(values):
    if not values or values[0] is None:
        return None
    iter_values = iter(values)
    root = Node(next(iter_values))
    queue = deque([root])
    for val in iter_values:
        node = queue.popleft()
        if val is not None:
            node.left = Node(val)
            queue.append(node.left)
        try:
            val = next(iter_values)
            if val is not None:
                node.right = Node(val)
                queue.append(node.right)
        except StopIteration:
            break
    return root

if __name__ == "__main__":
    obj = Solution()
    
    # Test Case 1
    root = build_tree([2, 1, 3])
    print(obj.kthSmallest(root, 2))  # Expected 2

    # Test Case 2
    root = build_tree([2, 1, 3])
    print(obj.kthSmallest(root, 5))  # Expected -1

    # Test Case 3
    root = build_tree([20, 8, 22, 4, 12, None, None, None, None, 10, 14])
    print(obj.kthSmallest(root, 3))  # Expected 10
