class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    # Utility: reverse a linked list
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    
    def addTwoLists(self, head1, head2):
        # Step 1: Reverse both lists
        l1 = self.reverseList(head1)
        l2 = self.reverseList(head2)
        
        dummy = Node(0)
        curr = dummy
        carry = 0
        
        # Step 2: Add corresponding digits
        while l1 or l2 or carry:
            val1 = l1.data if l1 else 0
            val2 = l2.data if l2 else 0
            
            total = val1 + val2 + carry
            carry = total // 10
            curr.next = Node(total % 10)
            curr = curr.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        # Step 3: Reverse result back
        result = self.reverseList(dummy.next)
        
        # Step 4: Remove leading zeros
        while result and result.data == 0 and result.next:
            result = result.next
        
        return result

# Helper function to print linked list
def printList(head):
    res = []
    while head:
        res.append(head.data)
        head = head.next
    print(res)

# Test cases
sol = Solution()

# Test case 1
head1 = Node(4); head1.next = Node(5)
head2 = Node(3); head2.next = Node(4); head2.next.next = Node(5)
ans1 = sol.addTwoLists(head1, head2)
printList(ans1)  # Output: [3, 9, 0]

# Test case 2
head3 = Node(0); head3.next = Node(0); head3.next.next = Node(6); head3.next.next.next = Node(3)
head4 = Node(0); head4.next = Node(7)
ans2 = sol.addTwoLists(head3, head4)
printList(ans2)  # Output: [7, 0]
