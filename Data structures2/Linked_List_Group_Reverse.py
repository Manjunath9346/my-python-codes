class Solution:
    def reverseKGroup(self, head, k):
        if not head or k <= 1:
            return head
        
        # Helper function to reverse a linked list segment
        def reverse_segment(start, end):
            prev, curr = None, start
            while prev != end:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        
        dummy = Node(0)
        dummy.next = head
        group_prev = dummy
        
        while True:
            kth = group_prev
            count = 0
            while count < k and kth.next:
                kth = kth.next
                count += 1
            # If we reached end before k nodes, still reverse as per problem
            if count == 0:
                break
            
            group_start = group_prev.next
            group_end = kth
            next_group = group_end.next
            
            # Reverse current group
            prev = next_group
            curr = group_start
            while curr != next_group:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            group_prev.next = prev
            group_prev = group_start
            
            if not next_group:
                break
        
        return dummy.next

# Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Utility functions
def list_to_linked(lst):
    if not lst:
        return None
    head = Node(lst[0])
    curr = head
    for val in lst[1:]:
        curr.next = Node(val)
        curr = curr.next
    return head

def linked_to_list(head):
    res = []
    while head:
        res.append(head.data)
        head = head.next
    return res

if __name__ == "__main__":
    obj = Solution()
    
    # Test Case 1
    head = list_to_linked([1, 2, 2, 4, 5, 6, 7, 8])
    k = 4
    new_head = obj.reverseKGroup(head, k)
    print(linked_to_list(new_head))  # Expected: [4, 2, 2, 1, 8, 7, 6, 5]
    
    # Test Case 2
    head = list_to_linked([1, 2, 3, 4, 5])
    k = 3
    new_head = obj.reverseKGroup(head, k)
    print(linked_to_list(new_head))  # Expected: [3, 2, 1, 5, 4]
