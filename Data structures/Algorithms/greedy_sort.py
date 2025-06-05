# User function Template for python3

class Solution:    
    # Function to find the minimum number of platforms required at the
    # railway station such that no train waits.
    def minimumPlatform(self, arr, dep):
        n = len(arr)
        
        # Sort both arrival and departure times
        arr.sort()
        dep.sort()
        
        platform_needed = 0
        max_platforms = 0
        
        i = 0  # pointer for arrival
        j = 0  # pointer for departure
        
        while i < n:
            # If next train arrives before previous one departs, need extra platform
            if arr[i] <= dep[j]:
                platform_needed += 1
                i += 1
            else:
                # One train departed
                platform_needed -= 1
                j += 1
            
            # Update max platforms needed
            max_platforms = max(max_platforms, platform_needed)
        
        return max_platforms
sol = Solution()
print(sol.minimumPlatform([900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000]))  # Output: 3
print(sol.minimumPlatform([900, 1235, 1100], [1000, 1240, 1200]))  # Output: 1
print(sol.minimumPlatform([1000, 935, 1100], [1200, 1240, 1130]))  # Output: 3
