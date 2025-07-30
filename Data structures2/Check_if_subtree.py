class Node:
    def __init__(self, val):  # ✅ fixed __init__ method
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def isIdentical(self, root1, root2):
        # If both are None, trees match
        if not root1 and not root2:
            return True
        # If one is None and the other isn't
        if not root1 or not root2:
            return False
        # Check data + left + right
        return (root1.data == root2.data and
                self.isIdentical(root1.left, root2.left) and
                self.isIdentical(root1.right, root2.right))

    def isSubTree(self, T, S):
        # If S is None, it's always a subtree
        if not S:
            return True
        # If T is None, S can't be a subtree
        if not T:
            return False
        # If identical from this node, return True
        if self.isIdentical(T, S):
            return True
        # Otherwise check in left or right subtree
        return self.isSubTree(T.left, S) or self.isSubTree(T.right, S)

#  TEST CASES
if __name__ == "__main__":
    obj = Solution()

    # Test Case 1 (Example 1)
    T = Node(1)
    T.left = Node(2)
    T.right = Node(3)
    T.right.left = Node(4)

    S = Node(3)
    S.left = Node(4)

    print(obj.isSubTree(T, S))  # Expected 1

    # Test Case 2 (Example 2)
    T = Node(26)
    T.left = Node(10)
    T.left.left = Node(20)
    T.left.right = Node(30)
    T.left.left.left = Node(40)
    T.left.left.right = Node(60)

    S = Node(26)
    S.left = Node(10)
    S.left.left = Node(20)
    S.left.right = Node(30)
    S.left.left.left = Node(40)
    S.left.left.right = Node(60)

    print(obj.isSubTree(T, S))  # Expected 1

    # Test Case 3 (Not a subtree)
    T = Node(1)
    T.left = Node(2)
    T.right = Node(3)

    S = Node(4)

    print(obj.isSubTree(T, S))  # Expected 0

    # Test Case 4 (Subtree with duplicate values)
    T = Node(5)
    T.left = Node(5)
    T.left.left = Node(5)

    S = Node(5)
    S.left = Node(5)

    print(obj.isSubTree(T, S)) 
