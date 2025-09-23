# Definition for a Binary Tree Node
class Node:
    def __init__(self, val=0):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def inorder(self, root, arr):
        if not root:
            return
        self.inorder(root.left, arr)
        arr.append(root.data)
        self.inorder(root.right, arr)
    
    def mergeSortedLists(self, arr1, arr2):
        i, j = 0, 0
        merged = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                merged.append(arr1[i])
                i += 1
            else:
                merged.append(arr2[j])
                j += 1
        while i < len(arr1):
            merged.append(arr1[i])
            i += 1
        while j < len(arr2):
            merged.append(arr2[j])
            j += 1
        return merged
    
    def merge(self, root1, root2):
        arr1, arr2 = [], []
        self.inorder(root1, arr1)
        self.inorder(root2, arr2)
        return self.mergeSortedLists(arr1, arr2)


# --------- Test Cases ----------
# Helper function to build tree from level-order list
from collections import deque

def buildTree(nodes):
    if not nodes or nodes[0] is None:
        return None
    root = Node(nodes[0])
    q = deque([root])
    i = 1
    while q and i < len(nodes):
        node = q.popleft()
        if i < len(nodes) and nodes[i] is not None:
            node.left = Node(nodes[i])
            q.append(node.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            node.right = Node(nodes[i])
            q.append(node.right)
        i += 1
    return root


sol = Solution()

# Example 1
root1 = buildTree([5, 3, 6, 2, 4])
root2 = buildTree([2, 1, 3, None, None, None, 7, 6])
print(sol.merge(root1, root2))  # Output: [1, 2, 2, 3, 3, 4, 5, 6, 6, 7]

# Example 2
root1 = buildTree([12, 9, None, 6, 11])
root2 = buildTree([8, 5, 10, 2])
print(sol.merge(root1, root2))  # Output: [2, 5, 6, 8, 9, 10, 11, 12]
