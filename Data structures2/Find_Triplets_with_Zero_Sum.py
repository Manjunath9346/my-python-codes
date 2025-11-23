class Solution:
    def findTriplets(self, arr):
        n = len(arr)
        res = set()   # store unique triplets

        arr_idx = [(arr[i], i) for i in range(n)]
        arr_idx.sort()

        for i in range(n - 2):
            a, ia = arr_idx[i]
            l, r = i + 1, n - 1

            while l < r:
                b, ib = arr_idx[l]
                c, ic = arr_idx[r]
                s = a + b + c

                if s == 0:
                    trip = tuple(sorted([ia, ib, ic]))
                    res.add(trip)
                    l += 1
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1

        # convert set of tuples to sorted list
        return [list(t) for t in sorted(res)]

sol = Solution()

print(sol.findTriplets([0, -1, 2, -3, 1]))
# Expected: [[0,1,4], [2,3,4]]

print(sol.findTriplets([1, -2, 1, 0, 5]))
# Expected: [[0,1,2]]

print(sol.findTriplets([2, 3, 1, 0, 5]))
# Expected: [[]]

print(sol.findTriplets([-1, -1, 2, 0, 1]))
# Example: [-1,-1,2] → indices sorted

print(sol.findTriplets([3, -3, 0]))
# Expected: [[0,1,2]]

print(sol.findTriplets([-5, 2, 3, 0, -3, 1]))
# Multiple triplets possible

print(sol.findTriplets([1,1,1]))
# No 0-sum triplet → [[]]
