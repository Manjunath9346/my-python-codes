class Solution:
    def bToDLL(self, root):
        # inorder traversal pointer tracking
        self.prev = None
        self.head = None

        def inorder(node):
            if not node:
                return
            
            # Left
            inorder(node.left)

            # Process current node
            if self.prev is None:
                # First (leftmost) node -> head of DLL
                self.head = node
            else:
                # Link prev <--> node
                self.prev.right = node
                node.left = self.prev

            # Move prev forward
            self.prev = node

            # Right
            inorder(node.right)

        inorder(root)
        return self.head


Input Tree: [1, 2, 3]

Inorder: 3,1,2  
Output DLL: 3 <-> 1 <-> 2
