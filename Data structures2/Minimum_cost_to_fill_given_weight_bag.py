class Solution:
    def minimumCost(self, n, w, cost):
        INF = 10**18
        dp = [INF] * (w + 1)
        dp[0] = 0

        for weight in range(1, n + 1):
            packet_cost = cost[weight - 1]
            if packet_cost == -1:
                continue

            for curr in range(weight, w + 1):
                dp[curr] = min(dp[curr], dp[curr - weight] + packet_cost)

        return -1 if dp[w] == INF else dp[w]
sol = Solution()

print(sol.minimumCost(5, 5, [20,10,4,50,100]))
# Expected: 14  (2kg + 3kg)

print(sol.minimumCost(5, 5, [-1,-1,4,3,-1]))
# Expected: -1  (cannot make 5 kg)

print(sol.minimumCost(3, 5, [1, 2, 3]))
# 1kg=1, 2kg=2, 3kg=3 → best = 2kg+3kg = 5

print(sol.minimumCost(4, 7, [3,5,-1,6]))
# Expected: 3+3+? 2kg unavailable so -1 → best: 1kg*7 → 21
