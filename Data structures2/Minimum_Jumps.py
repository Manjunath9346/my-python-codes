class Solution:
    def minJumps(self, arr):
        n = len(arr)
        
        # if first element is 0, cannot move anywhere
        if n == 0 or arr[0] == 0:
            return -1
        if n == 1:
            return 0
        
        # maxReach = farthest index we can reach
        # steps = steps we can still take
        # jumps = number of jumps taken
        maxReach = arr[0]
        steps = arr[0]
        jumps = 1
        
        for i in range(1, n):
            # reached the end
            if i == n - 1:
                return jumps
            
            # update maxReach
            maxReach = max(maxReach, i + arr[i])
            
            # use a step
            steps -= 1
            
            # if no steps left, must jump
            if steps == 0:
                jumps += 1
                # if current index is beyond maxReach, can't move forward
                if i >= maxReach:
                    return -1
                # reset steps for the new jump
                steps = maxReach - i
        
        return -1
print(Solution().minJumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))  # Expected 3
print(Solution().minJumps([1, 4, 3, 2, 6, 7]))  # Expected 2
print(Solution().minJumps([0, 10, 20]))  # Expected -1
print(Solution().minJumps([2, 3, 1, 1, 4]))  # Expected 2
