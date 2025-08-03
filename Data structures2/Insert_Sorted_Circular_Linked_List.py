class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def sortedInsert(self, head, data):
        new_node = Node(data)

        # Case 1: Empty list
        if not head:
            new_node.next = new_node
            return new_node

        current = head

        # Case 2: Insert before head (smallest element)
        if data <= head.data:
            # Find last node
            while current.next != head:
                current = current.next
            current.next = new_node
            new_node.next = head
            head = new_node
            return head

        # Case 3: Insert in middle or end
        while (current.next != head) and (current.next.data < data):
            current = current.next

        new_node.next = current.next
        current.next = new_node
        return head
def print_circular(head):
    result = []
    temp = head
    while True:
        result.append(temp.data)
        temp = temp.next
        if temp == head:
            break
    return result

if __name__ == "__main__":
    sol = Solution()

    # Test 1
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(4)
    head.next.next.next = head
    head = sol.sortedInsert(head, 2)
    print(print_circular(head))  # Expected [1, 2, 2, 4]

    # Test 2
    head = Node(1)
    head.next = Node(4)
    head.next.next = Node(7)
    head.next.next.next = Node(9)
    head.next.next.next.next = head
    head = sol.sortedInsert(head, 5)
    print(print_circular(head))  # Expected [1, 4, 5, 7, 9]
