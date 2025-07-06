class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

class Solution:
    def lca(self, root, n1, n2):
        if root is None:
            return None

        if root.data == n1 or root.data == n2:
            return root

        left = self.lca(root.left, n1, n2)
        right = self.lca(root.right, n1, n2)

        if left and right:
            return root
        return left if left else right

# Helper to build tree from list (level-order)
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

# Test cases: (tree_list, n1, n2, expected_lca)
test_cases = [
    ([1, 2, 3, 4, 5, 6, 7], 5, 6, 1),
    ([5, 2, 'N', 3, 4], 3, 4, 2),
    ([5, 2, 'N', 3, 4], 5, 4, 5),
    ([5, 2, 'N', 3, 4], 2, 4, 2),
    ([1, 2, 3], 2, 3, 1),
    ([10, 5, 15, 2, 7, 12, 20], 2, 7, 5),
    ([1, 2, 3], 2, 2, 2),
    ([1, 2, 3, 4, 5, 6, 7], 4, 7, 1),
    ([1, 2, 'N', 3, 'N', 4, 'N'], 3, 4, 3),
    ([1, 'N', 2, 'N', 3, 'N', 4], 3, 4, 3)
]

# Run test cases
sol = Solution()
for idx, (tree_list, n1, n2, expected) in enumerate(test_cases, 1):
    root = build_tree(tree_list)
    result = sol.lca(root, n1, n2)
    result_val = result.data if result else None
    status = " Passed" if result_val == expected else f" Failed (Expected {expected}, Got {result_val})"
    print(f"Test Case {idx}: LCA({n1}, {n2}) -> {result_val} => {status}")
