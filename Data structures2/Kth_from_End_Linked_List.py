class Solution:
    def getKthFromLast(self, head, k):
        slow = head
        fast = head
        
        # Move fast pointer k steps ahead
        for _ in range(k):
            if fast is None:
                return -1
            fast = fast.next
        
        # Move both until fast reaches end
        while fast:
            slow = slow.next
            fast = fast.next
        
        return slow.data if slow else -1
LinkedList: 1->2->3->4->5->6->7->8->9
k = 2
Output: 8
