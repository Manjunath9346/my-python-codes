'''
    Function Arguments: head of the original list.
    Return Type: head of the new list formed.
    {
        # Node Class
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
    }
'''

class Solution:
    def segregate(self, head):
        # Count the number of 0s, 1s, and 2s
        count = [0, 0, 0]

        current = head
        while current:
            count[current.data] += 1
            current = current.next

        # Update the linked list with sorted values
        current = head
        i = 0
        while current:
            while count[i] == 0:
                i += 1
            current.data = i
            count[i] -= 1
            current = current.next

        return head
# Input: 1 → 2 → 2 → 1 → 2 → 0 → 2 → 2
# Expected Output: 0 → 1 → 1 → 2 → 2 → 2 → 2 → 2
input_values = [1, 2, 2, 1, 2, 0, 2, 2]
# Input: 2 → 2 → 0 → 1
# Expected Output: 0 → 1 → 2 → 2
input_values = [2, 2, 0, 1]
