class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def boundaryTraversal(self, root):
        if not root:
            return []

        res = []

        # Check if a node is a leaf
        def is_leaf(node):
            return not node.left and not node.right

        # Add left boundary excluding leaves
        def add_left_boundary(node):
            curr = node.left
            while curr:
                if not is_leaf(curr):
                    res.append(curr.data)
                if curr.left:
                    curr = curr.left
                else:
                    curr = curr.right

        # Add all leaf nodes (L->R)
        def add_leaves(node):
            if node is None:
                return
            if is_leaf(node):
                res.append(node.data)
                return
            add_leaves(node.left)
            add_leaves(node.right)

        # Add right boundary excluding leaves (collected bottom-up)
        def add_right_boundary(node):
            curr = node.right
            temp = []
            while curr:
                if not is_leaf(curr):
                    temp.append(curr.data)
                if curr.right:
                    curr = curr.right
                else:
                    curr = curr.left
            # Add in reverse order
            res.extend(temp[::-1])

        # Root (if it's not a leaf)
        if not is_leaf(root):
            res.append(root.data)

        add_left_boundary(root)
        add_leaves(root)
        add_right_boundary(root)

        return res
# Sample Tree creation
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.right.left = Node(8)
root.left.right.right = Node(9)

sol = Solution()
print(sol.boundaryTraversal(root))  # Output: [1, 2, 4, 8, 9, 6, 7, 3]
