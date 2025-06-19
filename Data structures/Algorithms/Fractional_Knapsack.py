class Solution:
    def fractionalknapsack(self, val, wt, capacity):
        # Create a list of items with value, weight, and value-to-weight ratio
        items = sorted(
            [(val[i], wt[i], val[i] / wt[i]) for i in range(len(val))],
            key=lambda x: x[2],
            reverse=True
        )

        total_value = 0.0
        for value, weight, ratio in items:
            if capacity >= weight:
                capacity -= weight
                total_value += value
            else:
                total_value += ratio * capacity
                break

        return round(total_value, 6)
val = [60, 100, 120]
wt = [10, 20, 30]
capacity = 50
