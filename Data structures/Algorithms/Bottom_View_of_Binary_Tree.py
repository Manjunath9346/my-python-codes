from collections import deque

class Solution:
    def bottomView(self, root):
        if not root:
            return []
        
        # Map to store the last node at each horizontal distance
        hd_node_map = {}
        # Queue for level order traversal: stores pairs (node, horizontal_distance)
        q = deque([(root, 0)])
        
        while q:
            node, hd = q.popleft()
            # For bottom view, we overwrite existing entries at the same horizontal distance
            hd_node_map[hd] = node.data
            
            if node.left:
                q.append((node.left, hd - 1))
            if node.right:
                q.append((node.right, hd + 1))
        
        # Extract values in order of increasing horizontal distance
        return [hd_node_map[hd] for hd in sorted(hd_node_map)]
# Example to build tree manually and test
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(60)

sol = Solution()
print(sol.bottomView(root))  # Output: [40, 20, 60, 30]
