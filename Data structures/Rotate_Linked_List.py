class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    # Function to rotate a linked list.
    def rotate(self, head, k):
        if not head or not head.next or k == 0:
            return head

        # Compute the length of the list
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        k = k % length
        if k == 0:
            return head

        # Traverse to the (k)th node
        prev = None
        curr = head
        for _ in range(k):
            prev = curr
            curr = curr.next

        # Break the list and reattach
        prev.next = None
        tail.next = head
        return curr
def printList(node):
    while node:
        print(node.data, end=" -> " if node.next else "\n")
        node = node.next

# Create linked list: 10 -> 20 -> 30 -> 40 -> 50
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

sol = Solution()
rotated = sol.rotate(head, 4)
printList(rotated)  # Output: 50 -> 10 -> 20 -> 30 -> 40
