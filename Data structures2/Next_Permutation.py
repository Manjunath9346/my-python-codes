class Solution:
    def nextPermutation(self, arr):
        n = len(arr)
        i = n - 2

        # Step 1: Find the first decreasing element from the end
        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1

        if i >= 0:
            j = n - 1
            # Step 2: Find the next greater element to swap
            while arr[j] <= arr[i]:
                j -= 1
            # Step 3: Swap them
            arr[i], arr[j] = arr[j], arr[i]

        # Step 4: Reverse the suffix
        arr[i + 1:] = reversed(arr[i + 1:])
arr = [1, 2, 3, 6, 5, 4]
Solution().nextPermutation(arr)
print(arr)
