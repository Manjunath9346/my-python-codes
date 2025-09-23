# Definition for singly-linked list node
class node:
    def __init__(self, data):  
        self.data = data
        self.next = None

class Solution:
    def divide(self, head):
        if not head or not head.next:
            return head
        
        even_head = even_tail = None
        odd_head = odd_tail = None
        
        curr = head
        while curr:
            if curr.data % 2 == 0:  # Even node
                if not even_head:
                    even_head = even_tail = curr
                else:
                    even_tail.next = curr
                    even_tail = even_tail.next
            else:  # Odd node
                if not odd_head:
                    odd_head = odd_tail = curr
                else:
                    odd_tail.next = curr
                    odd_tail = odd_tail.next
            curr = curr.next
        
        # If no even nodes, return odd list
        if not even_head:
            return odd_head
        
        # Connect even list to odd list
        even_tail.next = odd_head
        
        # Make sure last odd node points to None
        if odd_tail:
            odd_tail.next = None
        
        return even_head


# -------- Helper functions for testing --------
def buildList(arr):
    if not arr: return None
    head = node(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = node(val)
        curr = curr.next
    return head

def printList(head):
    res = []
    while head:
        res.append(head.data)
        head = head.next
    print("->".join(map(str, res)))


# -------- Test Cases --------
sol = Solution()

head = buildList([17, 15, 8, 9, 2, 4, 6])
new_head = sol.divide(head)
printList(new_head)  # Output: 8->2->4->6->17->15->9

head = buildList([1, 3, 5, 7])
new_head = sol.divide(head)
printList(new_head)  # Output: 1->3->5->7
