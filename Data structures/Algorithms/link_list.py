# Node for linked list:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def addTwoLists(self, num1, num2):
        # Helper to reverse a linked list
        def reverse(head):
            prev = None
            while head:
                next_node = head.next
                head.next = prev
                prev = head
                head = next_node
            return prev

        # Reverse input lists
        num1 = reverse(num1)
        num2 = reverse(num2)

        carry = 0
        dummy = Node(-1)
        temp = dummy

        # Add digits one by one
        while num1 or num2 or carry:
            val1 = num1.data if num1 else 0
            val2 = num2.data if num2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            temp.next = Node(total % 10)
            temp = temp.next
            if num1: num1 = num1.next
            if num2: num2 = num2.next

        # Reverse the result to get the final sum in correct order
        return reverse(dummy.next)
# Helper to convert list to linked list
def list_to_linked(lst):
    head = Node(lst[0])
    current = head
    for val in lst[1:]:
        current.next = Node(val)
        current = current.next
    return head

# Helper to print linked list
def print_linked_list(node):
    while node:
        print(node.data, end=" -> " if node.next else "\n")
        node = node.next

sol = Solution()

# Test Case 1: 45 + 345 = 390
num1 = list_to_linked([4, 5])
num2 = list_to_linked([3, 4, 5])
res1 = sol.addTwoLists(num1, num2)
print_linked_list(res1)  # Output: 3 -> 9 -> 0

# Test Case 2: 0063 + 07 = 70
num3 = list_to_linked([0, 0, 6, 3])
num4 = list_to_linked([0, 7])
res2 = sol.addTwoLists(num3, num4)
print_linked_list(res2)  # Output: 7 -> 0
