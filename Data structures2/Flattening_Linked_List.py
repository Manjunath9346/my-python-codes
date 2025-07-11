class Solution:
    def merge(self, a, b):
        # Base cases
        if not a: return b
        if not b: return a
        
        # Choose smaller value node
        if a.data < b.data:
            result = a
            result.bottom = self.merge(a.bottom, b)
        else:
            result = b
            result.bottom = self.merge(a, b.bottom)
        
        result.next = None  # Important: set next to None
        return result

    def flatten(self, root):
        # Base case
        if not root or not root.next:
            return root
        
        # Recur for list on right
        root.next = self.flatten(root.next)
        
        # Merge this list with the right list
        root = self.merge(root, root.next)
        
        return root
# Helper function to create the complex structure
def build_linked_list(arr):
    head = None
    prev = None

    for sublist in arr:
        sub_head = Node(sublist[0])
        current = sub_head
        for data in sublist[1:]:
            current.bottom = Node(data)
            current = current.bottom

        if not head:
            head = sub_head
        else:
            prev.next = sub_head
        prev = sub_head

    return head

# Helper function to print flattened list
def print_flattened_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.bottom
    print("None")

# Example Test
arr = [
    [5, 7, 8, 30],
    [10, 20],
    [19, 22, 50],
    [28, 35, 40, 45]
]

head = build_linked_list(arr)
sol = Solution()
flat_head = sol.flatten(head)
print_flattened_list(flat_head)
# Output: 5 -> 7 -> 8 -> 10 -> 19 -> 20 -> 22 -> 28 -> 30 -> 35 -> 40 -> 45 -> 50 -> None
