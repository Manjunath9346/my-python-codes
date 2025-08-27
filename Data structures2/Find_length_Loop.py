class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def lengthOfLoop(self, head):
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # Loop detected
            if slow == fast:
                return self.countLoopLength(slow)
        
        return 0  # No loop
    
    def countLoopLength(self, node):
        count = 1
        temp = node.next
        while temp != node:
            count += 1
            temp = temp.next
        return count
# Helper to create a linked list with loop
def createLinkedListWithLoop(values, pos):
    head = Node(values[0])
    curr = head
    loop_node = None
    
    for i in range(1, len(values)):
        curr.next = Node(values[i])
        curr = curr.next
        if i == pos - 1:  # 1-based index
            loop_node = curr
    if pos != 0:
        curr.next = loop_node
    return head

sol = Solution()

# Example 1
head1 = createLinkedListWithLoop([1,2,3,4,5], 2)
print(sol.lengthOfLoop(head1))  # Output: 4

# Example 2
head2 = createLinkedListWithLoop([25,14,19,33,10], 3)
print(sol.lengthOfLoop(head2))  # Output: 3

# Example 3
head3 = createLinkedListWithLoop([1,2,3,4,5], 0)
print(sol.lengthOfLoop(head3))  # Output: 0
