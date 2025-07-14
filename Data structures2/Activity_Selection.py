class Solution:
    def activitySelection(self, start, finish):
        activities = list(zip(start, finish))
        activities.sort(key=lambda x: x[1])  # sort by finish time
        count = 1
        end_time = activities[0][1]
        for i in range(1, len(activities)):
            if activities[i][0] > end_time:
                count += 1
                end_time = activities[i][1]
        return count

# Test Cases
sol = Solution()
print(sol.activitySelection([1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9]))  # Output: 4
print(sol.activitySelection([10, 12, 20], [20, 25, 30]))             # Output: 1
print(sol.activitySelection([1, 3, 2, 5], [2, 4, 3, 6]))             # Output: 3
