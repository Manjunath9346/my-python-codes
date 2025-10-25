class Solution:
    def matchPairs(self, n, nuts, bolts):
        # Define the correct order
        order = ['!', '#', '$', '%', '&', '*', '?', '@', '^']
        # Sort both nuts and bolts according to this order
        nuts.sort(key=lambda x: order.index(x))
        bolts.sort(key=lambda x: order.index(x))
# Test 1
nuts = ['@', '%', '$', '#', '^']
bolts = ['%', '@', '#', '$', '^']
Solution().matchPairs(5, nuts, bolts)
print(nuts)  #  Output: ['#', '$', '%', '@', '^']
print(bolts) #  Output: ['#', '$', '%', '@', '^']

# Test 2
nuts = ['^', '&', '%', '@', '#', '*', '$', '?', '!']
bolts = ['?', '#', '@', '%', '&', '*', '$', '^', '!']
Solution().matchPairs(9, nuts, bolts)
print(nuts)  #  Output: ['!', '#', '$', '%', '&', '*', '?', '@', '^']
print(bolts) #  Output: ['!', '#', '$', '%', '&', '*', '?', '@', '^']
