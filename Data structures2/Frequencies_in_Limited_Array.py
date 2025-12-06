class Solution:
    def frequencyCount(self, arr):
        n = len(arr)
        freq = [0] * n   # result array

        # Count frequencies
        for num in arr:
            freq[num - 1] += 1   # num ranges 1..n → index num-1

        return freq
obj = Solution()

print(obj.frequencyCount([2, 3, 2, 3, 5]))  
# Expected: [0, 2, 2, 0, 1]

print(obj.frequencyCount([3, 3, 3, 3]))  
# Expected: [0, 0, 4, 0]

print(obj.frequencyCount([1]))  
# Expected: [1]

print(obj.frequencyCount([1, 2, 2, 1]))  
# Expected: [2, 2, 0, 0]
