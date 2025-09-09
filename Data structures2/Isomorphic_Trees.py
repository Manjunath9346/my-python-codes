class Solution:
    # Return True if the given trees are isomorphic. Else return False.
    def isIsomorphic(self, root1, root2):
        # Both trees empty
        if root1 is None and root2 is None:
            return True
        # One tree empty
        if root1 is None or root2 is None:
            return False
        # Data mismatch
        if root1.data != root2.data:
            return False
        
        # Check without swapping OR with swapping
        return ((self.isIsomorphic(root1.left, root2.left) and
                 self.isIsomorphic(root1.right, root2.right)) or
                (self.isIsomorphic(root1.left, root2.right) and
                 self.isIsomorphic(root1.right, root2.left)))
# Tree Node definition
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Build trees from array (level order)
def build_tree(arr):
    if not arr or arr[0] == 'N':
        return None
    root = Node(arr[0])
    q = [root]
    i = 1
    while q and i < len(arr):
        curr = q.pop(0)
        if i < len(arr) and arr[i] != 'N':
            curr.left = Node(arr[i])
            q.append(curr.left)
        i += 1
        if i < len(arr) and arr[i] != 'N':
            curr.right = Node(arr[i])
            q.append(curr.right)
        i += 1
    return root

# Test Cases
sol = Solution()

root1 = build_tree([1,2,3,4,5,7,6,'N',7,8])
root2 = build_tree([1,3,2,'N',6,4,5,8,7])
print(sol.isIsomorphic(root1, root2))  # True

root1 = build_tree([1,2,3,4])
root2 = build_tree([1,3,2,4])
print(sol.isIsomorphic(root1, root2))  # False

root1 = build_tree([1,2,3,4])
root2 = build_tree([1,3,2,'N','N','N',4])
print(sol.isIsomorphic(root1, root2))  # True
