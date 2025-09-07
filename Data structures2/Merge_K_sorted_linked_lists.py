import heapq

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class Solution:
    def mergeKLists(self, arr):
        # Min-heap to store (node value, list index, node reference)
        heap = []
        for i, node in enumerate(arr):
            if node:
                heapq.heappush(heap, (node.data, i, node))
        
        dummy = Node(0)
        curr = dummy
        
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.data, i, node.next))
        
        return dummy.next


# --------------------------
# Helper functions for tests
# --------------------------
def build_linked_list(arr):
    if not arr: return None
    head = Node(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = Node(val)
        curr = curr.next
    return head

def print_linked_list(head):
    res = []
    while head:
        res.append(str(head.data))
        head = head.next
    return " -> ".join(res)


# Test Cases
sol = Solution()

# Example 1
list1 = build_linked_list([1, 3, 7])
list2 = build_linked_list([2, 4, 8])
list3 = build_linked_list([9])
merged = sol.mergeKLists([list1, list2, list3])
print(print_linked_list(merged))  # Output: 1 -> 2 -> 3 -> 4 -> 7 -> 8 -> 9

# Example 2
list1 = build_linked_list([1, 3])
list2 = build_linked_list([8])
list3 = build_linked_list([4, 5, 6])
merged = sol.mergeKLists([list1, list2, list3])
print(print_linked_list(merged))  # Output: 1 -> 3 -> 4 -> 5 -> 6 -> 8

# Edge Case: Single list
list1 = build_linked_list([1, 2, 3])
merged = sol.mergeKLists([list1])
print(print_linked_list(merged))  # Output: 1 -> 2 -> 3

# Edge Case: Empty lists
merged = sol.mergeKLists([None, None])
print(print_linked_list(merged))  # Output: (empty string)
