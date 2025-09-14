# Node class assumed:
# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

class Solution:
    def dupSub(self, root):
        # map subtree-key -> unique id
        id_map = {}
        # count occurrences of each subtree id
        freq = {}
        next_id = 1
        found = [False]

        def dfs(node):
            nonlocal next_id
            if node is None:
                return 0, 0   # id 0 reserved for null, size 0

            left_id, left_size = dfs(node.left)
            right_id, right_size = dfs(node.right)

            key = (node.data, left_id, right_id)
            if key in id_map:
                cur_id = id_map[key]
            else:
                cur_id = next_id
                id_map[key] = cur_id
                next_id += 1

            size = 1 + left_size + right_size
            freq[cur_id] = freq.get(cur_id, 0) + 1

            # only subtrees of size >= 2 count (exclude single-node leaves)
            if freq[cur_id] > 1 and size > 1:
                found[0] = True

            return cur_id, size

        dfs(root)
        return 1 if found[0] else 0
# helper Node
class Node:
    def __init__(self, v):
        self.data = v
        self.left = None
        self.right = None

sol = Solution()

# Example: duplicate subtree exists
r = Node(1)
r.left = Node(2)
r.right = Node(3)
r.left.left = Node(4)
r.left.right = Node(5)
r.right.right = Node(2)
r.right.right.left = Node(4)
r.right.right.right = Node(5)
print(sol.dupSub(r))   # 1

# Example: only duplicate leaves (should NOT count)
r2 = Node(1)
r2.left = Node(1)
r2.right = Node(1)
print(sol.dupSub(r2))  # 0

# Example: no duplicates
r3 = Node(1)
r3.left = Node(2)
r3.right = Node(3)
print(sol.dupSub(r3))  # 0
