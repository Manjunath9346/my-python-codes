class Solution:
    def deleteNode(self, del_node):
        if del_node is None or del_node.next is None:
            return  # can't delete if it's the last node or None
        
        # Copy data from next node
        del_node.data = del_node.next.data
        # Bypass next node
        del_node.next = del_node.next.next
# Helper function to print list
def printList(head):
    res = []
    while head:
        res.append(head.data)
        head = head.next
    return res

# Create linked list: 1 -> 2
head = Node(1)
head.next = Node(2)

sol = Solution()
sol.deleteNode(head)  # delete node 1 (actually replaced by next)
print(printList(head))  # [2]

# Linked list: 10 -> 20 -> 4 -> 30
head = Node(10)
head.next = Node(20)
head.next.next = Node(4)
head.next.next.next = Node(30)

sol.deleteNode(head.next)  # delete node with value 20
print(printList(head))  # [10, 4, 30]
