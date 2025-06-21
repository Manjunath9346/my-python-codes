class Solution:
    def jobSequencing(self, deadline, profit):
        n = len(deadline)
        jobs = sorted(zip(deadline, profit), key=lambda x: -x[1])
        
        max_deadline = max(deadline)
        parent = [i for i in range(max_deadline + 1)]

        # Find with path compression
        def find(slot):
            if parent[slot] == slot:
                return slot
            parent[slot] = find(parent[slot])
            return parent[slot]

        # Merge two sets
        def merge(u, v):
            parent[u] = v

        count_jobs = 0
        total_profit = 0

        for d, p in jobs:
            available_slot = find(d)
            if available_slot > 0:
                merge(available_slot, find(available_slot - 1))
                count_jobs += 1
                total_profit += p

        return [count_jobs, total_profit]
sol = Solution()
print(sol.jobSequencing([4, 1, 1, 1], [20, 10, 40, 30]))  # Output: [2, 60]
print(sol.jobSequencing([2, 1, 2, 1, 1], [100, 19, 27, 25, 15]))  # Output: [2, 127]
