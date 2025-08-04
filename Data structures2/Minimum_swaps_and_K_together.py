class Solution:
    def minSwap(self, arr, k):
        n = len(arr)
        
        # Step 1: Count elements <= k
        count_good = sum(1 for num in arr if num <= k)
        
        if count_good == 0 or count_good == 1:
            return 0  # No swap needed
        
        # Step 2: Count bad elements in first window
        bad = sum(1 for i in range(count_good) if arr[i] > k)
        
        # Step 3: Slide the window
        ans = bad
        for i in range(count_good, n):
            if arr[i - count_good] > k:
                bad -= 1
            if arr[i] > k:
                bad += 1
            ans = min(ans, bad)
        
        return ans
if __name__ == "__main__":
    sol = Solution()
    print(sol.minSwap([2, 1, 5, 6, 3], 3))  # Expected 1
    print(sol.minSwap([2, 7, 9, 5, 8, 7, 4], 6))  # Expected 2
    print(sol.minSwap([2, 4, 5, 3, 6, 1, 8], 6))  # Expected 0
