class Solution:
    def heapify(self, arr, n, i):
        largest = i
        l, r = 2*i+1, 2*i+2
        if l < n and arr[l] > arr[largest]: largest = l
        if r < n and arr[r] > arr[largest]: largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    def heapSort(self, arr):
        n = len(arr)
        for i in range(n//2-1, -1, -1):  # Build max-heap
            self.heapify(arr, n, i)
        for i in range(n-1, 0, -1):  # Extract elements
            arr[0], arr[i] = arr[i], arr[0]
            self.heapify(arr, i, 0)
s = Solution()

arr1 = [4, 1, 3, 9, 7]
s.heapSort(arr1)
print(arr1)  # [1, 3, 4, 7, 9]

arr2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
s.heapSort(arr2)
print(arr2)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

arr3 = [2, 1, 5]
s.heapSort(arr3)
print(arr3)  # [1, 2, 5]
