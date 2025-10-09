
# Tree Node
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    # Function to find the least absolute difference between any node value of the BST and the given integer.
    def minDiff(self, root, K):
        diff = float('inf')
        curr = root
        
        # Traverse BST like binary search
        while curr:
            diff = min(diff, abs(curr.data - K))
            
            # Move left if K is smaller, right if K is greater
            if K < curr.data:
                curr = curr.left
            elif K > curr.data:
                curr = curr.right
            else:
                # Exact match
                return 0
        
        return diff

# Test Cases:


# Example 1
# Tree: 10 / 2 11 / 1 5 / 3 6 / 4
root = Node(10)
root.left = Node(2)
root.right = Node(11)
root.left.left = Node(1)
root.left.right = Node(5)
root.left.right.left = Node(3)
root.left.right.right = Node(6)
root.left.right.left.right = Node(4)
print(Solution().minDiff(root, 13))  # Output: 2

# Example 2
root = Node(8)
root.left = Node(1)
root.right = Node(9)
root.left.right = Node(4)
root.left.right.left = Node(3)
root.right.right = Node(10)
print(Solution().minDiff(root, 9))  # Output: 0

