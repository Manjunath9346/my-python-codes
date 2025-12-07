class Solution:
    def getMiddle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data
# Example: 1 → 2 → 3 → 4 → 5
print(obj.getMiddle(head))  
# Output: 3

# Example: 2 → 4 → 6 → 7 → 5 → 1
print(obj.getMiddle(head))  
# Output: 7
