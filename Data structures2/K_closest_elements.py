class Solution:
    def printKClosest(self, arr, k, x):
        # Remove x if it exists
        arr = [num for num in arr if num != x]
        
        # Sort based on closeness, with tie-breaking rule (prefer larger element)
        arr.sort(key=lambda num: (abs(num - x), -num))
        
        # Take first k elements
        return arr[:k]

# Example Test Cases
if __name__ == "__main__":
    sol = Solution()
    
    arr1 = [1, 3, 4, 10, 12]
    k1 = 2
    x1 = 4
    print(sol.printKClosest(arr1, k1, x1))  # Output: [3, 1]

    arr2 = [12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56]
    k2 = 4
    x2 = 35
    print(sol.printKClosest(arr2, k2, x2))  # Output: [39, 30, 42, 45]

    arr3 = [5, 6, 7, 8, 9]
    k3 = 3
    x3 = 7
    print(sol.printKClosest(arr3, k3, x3))  # Output: [8, 6, 9]
