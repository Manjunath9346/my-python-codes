# Node class for singly linked list
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Solution:
    def removeLoop(self, head):
        if not head or not head.next:
            return

        slow = head
        fast = head

        # Step 1: Detect Loop using Floyd's cycle detection
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            # No loop
            return

        # Step 2: Find start of loop
        slow = head
        if slow == fast:
            # Special case: Loop starts at head
            while fast.next != slow:
                fast = fast.next
        else:
            while slow.next != fast.next:
                slow = slow.next
                fast = fast.next

        # Step 3: Break the loop
        fast.next = None
