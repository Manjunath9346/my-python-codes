class Solution:
    def reverse(self, St):
        # Helper function to insert element at bottom of stack
        def insert_at_bottom(stack, item):
            if not stack:
                stack.append(item)
            else:
                temp = stack.pop()
                insert_at_bottom(stack, item)
                stack.append(temp)

        # Main reverse function (recursive)
        if St:
            temp = St.pop()
            self.reverse(St)
            insert_at_bottom(St, temp)
        return St
# Test case 1
St = [3,2,1,7,6]
print(Solution().reverse(St))  # Expected: [6,7,1,2,3]

# Test case 2
St = [4,3,9,6]
print(Solution().reverse(St))  # Expected: [6,9,3,4]

# Test case 3
St = [1]
print(Solution().reverse(St))  # Expected: [1]

# Test case 4
St = [10,20,30,40,50]
print(Solution().reverse(St))  # Expected: [50,40,30,20,10]

# Test case 5
St = []
print(Solution().reverse(St))  # Expected: []
