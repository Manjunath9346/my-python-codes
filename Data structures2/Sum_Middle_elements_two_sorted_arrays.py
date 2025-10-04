class Solution:
    def sum_of_middle_elements(self, arr1, arr2):
        n = len(arr1)
        
        # Ensure arr1 is the smaller array for binary search
        if n == 0:
            return -1

        low, high = 0, n
        while low <= high:
            cut1 = (low + high) // 2
            cut2 = n - cut1
            
            l1 = float('-inf') if cut1 == 0 else arr1[cut1 - 1]
            l2 = float('-inf') if cut2 == 0 else arr2[cut2 - 1]
            r1 = float('inf') if cut1 == n else arr1[cut1]
            r2 = float('inf') if cut2 == n else arr2[cut2]
            
            if l1 <= r2 and l2 <= r1:
                # Found correct partition
                left_max = max(l1, l2)
                right_min = min(r1, r2)
                return left_max + right_min
            elif l1 > r2:
                high = cut1 - 1
            else:
                low = cut1 + 1
        
        return -1  # Should never reach here if inputs are valid


# Example Test Cases
if __name__ == "__main__":
    sol = Solution()

    arr1 = [1, 2, 4, 6, 10]
    arr2 = [4, 5, 6, 9, 12]
    print(sol.sum_of_middle_elements(arr1, arr2))  # Output: 11

    arr1 = [1, 12, 15, 26, 38]
    arr2 = [2, 13, 17, 30, 45]
    print(sol.sum_of_middle_elements(arr1, arr2))  # Output: 32

    arr1 = [2, 3, 5, 8]
    arr2 = [10, 12, 14, 16]
    print(sol.sum_of_middle_elements(arr1, arr2))  # Output: 13
