#User function Template for python3

class Solution:
    def search(self, n, arr):
        low, high = 0, n - 1

        while low < high:
            mid = (low + high) // 2

            # Ensure mid is even
            if mid % 2 == 1:
                mid -= 1

            if arr[mid] == arr[mid + 1]:
                low = mid + 2
            else:
                high = mid

        return arr[low]


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    arr1 = [1, 1, 2, 5, 5]
    print("Input:", arr1, "→ Output:", sol.search(len(arr1), arr1))  # Expected: 2

    # Example 2
    arr2 = [2, 2, 5, 5, 20, 30, 30]
    print("Input:", arr2, "→ Output:", sol.search(len(arr2), arr2))  # Expected: 20

    # Edge Case: Single element
    arr3 = [7]
    print("Input:", arr3, "→ Output:", sol.search(len(arr3), arr3))  # Expected: 7

    # Edge Case: Unique at start
    arr4 = [4, 5, 5, 6, 6, 7, 7]
    print("Input:", arr4, "→ Output:", sol.search(len(arr4), arr4))  # Expected: 4

    # Edge Case: Unique at end
    arr5 = [1, 1, 2, 2, 3, 3, 9]
    print("Input:", arr5, "→ Output:", sol.search(len(arr5), arr5))  # Expected: 9

    # Larger case
    arr6 = [1,1,2,2,3,3,4,4,10,11,11,12,12]
    print("Input:", arr6, "→ Output:", sol.search(len(arr6), arr6))  # Expected: 10
