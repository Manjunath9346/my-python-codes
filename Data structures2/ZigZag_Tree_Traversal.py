class Solution:
    # Function to store the zig zag order traversal of tree in a list.
    def zigZagTraversal(self, root):
        if not root:
            return []

        result = []
        queue = [root]
        left_to_right = True

        while queue:
            level_size = len(queue)
            level_nodes = []

            for _ in range(level_size):
                node = queue.pop(0)
                level_nodes.append(node.data)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Append current level based on direction
            if left_to_right:
                result.extend(level_nodes)
            else:
                result.extend(level_nodes[::-1])

            left_to_right = not left_to_right  # Toggle direction

        return result
# Helper function to build tree (for test only)
def build_example_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    return root

sol = Solution()
root = build_example_tree()
print(sol.zigZagTraversal(root))
# Output: [1, 3, 2, 4, 5, 6, 7]
