# Node class is already provided by GFG
class Solution:
    def sortedMerge(self, head1, head2):
        dummy = Node(-1)
        tail = dummy

        while head1 and head2:
            if head1.data <= head2.data:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next

        if head1:
            tail.next = head1
        else:
            tail.next = head2

        return dummy.next
# Helper functions for testing

def create_linked_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        current.next = Node(val)
        current = current.next
    return head

def print_linked_list(head):
    result = []
    while head:
        result.append(str(head.data))
        head = head.next
    print(" -> ".join(result))

# Test Case 1
l1 = create_linked_list([5, 10, 15, 40])
l2 = create_linked_list([2, 3, 20])
sol = Solution()
merged = sol.sortedMerge(l1, l2)
print_linked_list(merged)  # Output: 2 -> 3 -> 5 -> 10 -> 15 -> 20 -> 40

# Test Case 2
l1 = create_linked_list([1, 1])
l2 = create_linked_list([2, 4])
merged = sol.sortedMerge(l1, l2)
print_linked_list(merged)  # Output: 1 -> 1 -> 2 -> 4
