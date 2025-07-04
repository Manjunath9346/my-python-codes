from collections import defaultdict, deque

class Solution:
    def verticalOrder(self, root):
        if not root:
            return []

        col_table = defaultdict(list)
        queue = deque([(root, 0)])  # (node, column_index)
        min_col = max_col = 0

        while queue:
            node, col = queue.popleft()
            col_table[col].append(node.data)
            min_col = min(min_col, col)
            max_col = max(max_col, col)
            
            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))

        return [col_table[i] for i in range(min_col, max_col + 1)]
# Helper to build tree from level order
def buildTree(values):
    if not values or values[0] == 'N':
        return None
    root = Node(int(values[0]))
    q = deque([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if values[i] != 'N':
            node.left = Node(int(values[i]))
            q.append(node.left)
        i += 1
        if i < len(values) and values[i] != 'N':
            node.right = Node(int(values[i]))
            q.append(node.right)
        i += 1
    return root

# Example usage
vals = [1, 2, 3, 4, 5, 'N', 6]
root = buildTree(vals)
sol = Solution()
print(sol.verticalOrder(root))  # Output: [[4], [2], [1, 5], [3], [6]]
