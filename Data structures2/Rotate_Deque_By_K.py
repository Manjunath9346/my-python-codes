from collections import deque

class Solution:    
    def rotateDeque(self, dq, type, k):
        n = len(dq)
        k = k % n  # to avoid extra full rotations

        if type == 1:  # Right rotation
            dq.rotate(k)
        elif type == 2:  # Left rotation
            dq.rotate(-k)
        
        return list(dq)
if __name__ == "__main__":
    sol = Solution()

    dq1 = deque([1, 2, 3, 4, 5, 6])
    print(sol.rotateDeque(dq1, 1, 2))  # Expected [5, 6, 1, 2, 3, 4]

    dq2 = deque([10, 20, 30, 40, 50])
    print(sol.rotateDeque(dq2, 2, 3))  # Expected [40, 50, 10, 20, 30]

    dq3 = deque([7, 8, 9])
    print(sol.rotateDeque(dq3, 1, 5))  # Expected [8, 9, 7] (5 % 3 = 2)

    dq4 = deque([100])
    print(sol.rotateDeque(dq4, 2, 10))  # Expected [100] (only one element)

    dq5 = deque([1, 2, 3, 4])
    print(sol.rotateDeque(dq5, 2, 4))  # Expected [1, 2, 3, 4] (rotation by size)
