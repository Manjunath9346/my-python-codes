from collections import deque

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        
        result = []
        q = deque([root])
        
        while q:
            level = []
            size = len(q)
            
            for _ in range(size):
                node = q.popleft()
                level.append(node.data)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            result.append(level)
        
        return result
# Helper function to build tree from list (like Leetcode style)
def buildTree(arr):
    if not arr or arr[0] == "N":
        return None
    
    root = Node(arr[0])
    q = deque([root])
    i = 1
    
    while q and i < len(arr):
        curr = q.popleft()
        
        if arr[i] != "N":
            curr.left = Node(arr[i])
            q.append(curr.left)
        i += 1
        
        if i < len(arr) and arr[i] != "N":
            curr.right = Node(arr[i])
            q.append(curr.right)
        i += 1
    
    return root


sol = Solution()

# Example 1
root1 = buildTree([1, 2, 3])
print(sol.levelOrder(root1))  # [[1], [2, 3]]

# Example 2
root2 = buildTree([10, 20, 30, 40, 50])
print(sol.levelOrder(root2))  # [[10], [20, 30], [40, 50]]

# Example 3
root3 = buildTree([1, 3, 2, "N", "N", "N", 4, 6, 5])
print(sol.levelOrder(root3))  # [[1], [3, 2], [4], [6, 5]]
