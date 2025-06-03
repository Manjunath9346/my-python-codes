class Solution:
    # Function to count inversions in the array.
    def inversionCount(self, arr):
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr, 0

            mid = len(arr) // 2
            left, inv_left = merge_sort(arr[:mid])
            right, inv_right = merge_sort(arr[mid:])
            merged, inv_merge = merge(left, right)

            total_inversions = inv_left + inv_right + inv_merge
            return merged, total_inversions

        def merge(left, right):
            result = []
            i = j = inv_count = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    inv_count += len(left) - i  # Count inversions
                    j += 1

            result.extend(left[i:])
            result.extend(right[j:])
            return result, inv_count

        # Start the merge sort and get the inversion count
        _, total_inversions = merge_sort(arr)
        return total_inversions


# Driver Code
if __name__ == "__main__":
    # Example 1
    arr1 = [2, 4, 1, 3, 5]
    sol = Solution()
    print("Inversion Count:", sol.inversionCount(arr1))  # Output: 3

    # Example 2
    arr2 = [2, 3, 4, 5, 6]
    print("Inversion Count:", sol.inversionCount(arr2))  # Output: 0

    # Example 3
    arr3 = [10, 10, 10]
    print("Inversion Count:", sol.inversionCount(arr3))  # Output: 0

