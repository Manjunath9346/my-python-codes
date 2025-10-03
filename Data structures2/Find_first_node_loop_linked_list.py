class Solution:
    def cycleStart(self, head):
        slow = fast = head
        
        # Step 1: Detect if a cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  # Cycle detected
                break
        else:
            return -1  # No cycle
        
        # Step 2: Find start node of the cycle
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow.data  # Return the data of the first node in the loop

# Example Test Cases
if __name__ == "__main__":
    # Helper function to create a linked list with a loop
    def create_linked_list(values, pos):
        nodes = [Node(val) for val in values]
        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]
        if pos != 0:
            nodes[-1].next = nodes[pos-1]
        return nodes[0]

    # Test Case 1: Loop starts at node with value 3
    head1 = create_linked_list([1,2,3,4,5], 3)
    sol = Solution()
    print(sol.cycleStart(head1))  # Output: 3

    # Test Case 2: No loop
    head2 = create_linked_list([1,2,3,4,5], 0)
    print(sol.cycleStart(head2))  # Output: -1
