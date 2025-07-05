class Solution:
    def startStation(self, gas, cost):
        total_gas = 0
        total_cost = 0
        tank = 0
        start_index = 0
        
        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            tank += gas[i] - cost[i]
            
            if tank < 0:
                # Can't reach this station, so restart from next
                start_index = i + 1
                tank = 0

        if total_gas < total_cost:
            return -1  # Not possible to complete the circuit

        return start_index
gas = [4, 5, 7, 4]
cost = [6, 6, 3, 5]
s = Solution()
print(s.startStation([4, 5, 7, 4], [6, 6, 3, 5]))     # Output: 2
print(s.startStation([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))  # Output: 3
print(s.startStation([3, 9], [7, 6]))                # Output: -1
print(s.startStation([5, 1, 2, 3, 4], [4, 4, 1, 5, 1]))  # Output: 4
