class Solution:
    def reverse(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    def addOne(self, head):
        # Step 1: Reverse the linked list
        head = self.reverse(head)

        # Step 2: Add 1 to the number
        current = head
        carry = 1
        prev = None

        while current and carry:
            current.data += carry
            if current.data < 10:
                carry = 0
            else:
                current.data = 0
                carry = 1
            prev = current
            current = current.next

        # If there is still a carry, add a new node at the end
        if carry:
            prev.next = Node(1)

        # Step 3: Reverse the list back to original order
        head = self.reverse(head)
        return head
sol = Solution()

# Test Case 1: 1 -> 2 -> 3 => 1 -> 2 -> 4
head1 = createLinkedList([1, 2, 3])
result1 = sol.addOne(head1)
print("Test Case 1 Output:")
printList(result1)  # Expected: 1 -> 2 -> 4

# Test Case 2: 4 -> 5 -> 6 => 4 -> 5 -> 7
head2 = createLinkedList([4, 5, 6])
result2 = sol.addOne(head2)
print("Test Case 2 Output:")
printList(result2)  # Expected: 4 -> 5 -> 7

# Test Case 3: 9 -> 9 -> 9 => 1 -> 0 -> 0 -> 0
head3 = createLinkedList([9, 9, 9])
result3 = sol.addOne(head3)
print("Test Case 3 Output:")
printList(result3)  # Expected: 1 -> 0 -> 0 -> 0

# Test Case 4: Single node 0 => 1
head4 = createLinkedList([0])
result4 = sol.addOne(head4)
print("Test Case 4 Output:")
printList(result4)  # Expected: 1

# Test Case 5: 1 -> 9 -> 9 => 2 -> 0 -> 0
head5 = createLinkedList([1, 9, 9])
result5 = sol.addOne(head5)
print("Test Case 5 Output:")
printList(result5)  # Expected: 2 -> 0 -> 0
