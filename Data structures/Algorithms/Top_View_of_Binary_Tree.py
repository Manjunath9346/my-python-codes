from collections import deque

# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None

class Solution:
    # Function to return a list of nodes visible from the top view from left to right in Binary Tree.
    def topView(self, root):
        if not root:
            return []

        q = deque()  # Queue for BFS: stores (node, horizontal distance)
        top_view_map = {}  # Map to store first node at each horizontal distance
        min_hd = max_hd = 0  # Track the min and max horizontal distance

        q.append((root, 0))

        while q:
            node, hd = q.popleft()

            # If this horizontal distance is not in the map, we add it
            if hd not in top_view_map:
                top_view_map[hd] = node.data

            # Update min and max horizontal distances
            min_hd = min(min_hd, hd)
            max_hd = max(max_hd, hd)

            # Add left and right children to queue
            if node.left:
                q.append((node.left, hd - 1))
            if node.right:
                q.append((node.right, hd + 1))

        # Extract top view from the map in order from min_hd to max_hd
        result = []
        for hd in range(min_hd, max_hd + 1):
            if hd in top_view_map:
                result.append(top_view_map[hd])

        return result
