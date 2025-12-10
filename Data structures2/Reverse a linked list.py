class Solution:
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next   # save next
            curr.next = prev        # reverse the link
            prev = curr             # move prev forward
            curr = next_node        # move curr forward

        return prev   # new head
