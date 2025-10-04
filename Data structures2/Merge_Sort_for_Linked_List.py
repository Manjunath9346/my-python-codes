class Solution:
    def mergeSort(self, head):
        # Base case: if head is None or single node
        if not head or not head.next:
            return head
        
        # Step 1: Split list into two halves
        mid = self.getMiddle(head)
        next_to_mid = mid.next
        mid.next = None  # Break the list into two
        
        # Step 2: Recursively sort both halves
        left = self.mergeSort(head)
        right = self.mergeSort(next_to_mid)
        
        # Step 3: Merge sorted halves
        sorted_list = self.sortedMerge(left, right)
        return sorted_list
    
    # Helper: merge two sorted linked lists
    def sortedMerge(self, a, b):
        if not a:
            return b
        if not b:
            return a
        
        if a.data <= b.data:
            result = a
            result.next = self.sortedMerge(a.next, b)
        else:
            result = b
            result.next = self.sortedMerge(a, b.next)
        return result
    
    # Helper: find middle of linked list
    def getMiddle(self, head):
        if not head:
            return head
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow


# Example Test Cases
if __name__ == "__main__":
    # Helper to create linked list from Python list
    def create_linked_list(arr):
        if not arr:
            return None
        head = Node(arr[0])
        curr = head
        for val in arr[1:]:
            curr.next = Node(val)
            curr = curr.next
        return head
    
    # Helper to print linked list
    def print_list(head):
        res = []
        while head:
            res.append(str(head.data))
            head = head.next
        print(" -> ".join(res))
    
    sol = Solution()
    
    head1 = create_linked_list([40, 20, 60, 10, 50, 30])
    sorted_head1 = sol.mergeSort(head1)
    print_list(sorted_head1)  # Output: 10 -> 20 -> 30 -> 40 -> 50 -> 60
    
    head2 = create_linked_list([9, 8, 5, 2])
    sorted_head2 = sol.mergeSort(head2)
    print_list(sorted_head2)  # Output: 2 -> 5 -> 8 -> 9
