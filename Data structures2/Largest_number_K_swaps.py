#User function Template for python3

class Solution:
    
    #Function to find the largest number after k swaps.
    def findMaximumNum(self, s, k):
        self.max_num = s
        n = len(s)

        def helper(s_list, k, idx):
            if k == 0 or idx == n:
                return
            
            # find the maximum digit in the remaining substring
            max_digit = max(s_list[idx:])
            
            # if max_digit is same as current, no swap needed
            if max_digit != s_list[idx]:
                k -= 1  # we will perform a swap

            # try swapping with all positions where max_digit occurs
            for i in range(n-1, idx-1, -1):
                if s_list[i] == max_digit:
                    # swap
                    s_list[idx], s_list[i] = s_list[i], s_list[idx]

                    curr = "".join(s_list)
                    if curr > self.max_num:
                        self.max_num = curr
                    
                    helper(s_list, k, idx+1)
                    
                    # backtrack
                    s_list[idx], s_list[i] = s_list[i], s_list[idx]

        helper(list(s), k, 0)
        return self.max_num
ob = Solution()
print(ob.findMaximumNum("1234567", 4))   # 7654321
print(ob.findMaximumNum("3435335", 3))   # 5543333
print(ob.findMaximumNum("1034", 2))      # 4301
