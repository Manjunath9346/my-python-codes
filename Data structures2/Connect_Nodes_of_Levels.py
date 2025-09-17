class Solution:
    def connect(self, root):
        if not root:
            return None
        
        from collections import deque
        q = deque([root])
        
        while q:
            size = len(q)
            prev = None
            
            for _ in range(size):
                node = q.popleft()
                
                if prev:
                    prev.nextRight = node
                prev = node
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            # Last node in level points to None
            prev.nextRight = None
        
        return root
# Example 1
# Tree: [1, 2, 3, 4, 5, N, 6]
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

sol = Solution()
sol.connect(root)

# Level order traversal with nextRight:
# Output should be: [1, #, 2, 3, #, 4, 5, 6, #]
