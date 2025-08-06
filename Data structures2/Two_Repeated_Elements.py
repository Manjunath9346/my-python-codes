class Solution:
    def twoRepeated(self, arr):
        seen = set()
        result = []
        
        for num in arr:
            if num in seen:
                result.append(num)
                if len(result) == 2:
                    break
            else:
                seen.add(num)
        
        return result
if __name__ == "__main__":
    sol = Solution()
    print(sol.twoRepeated([1, 2, 1, 3, 4, 3]))  # Expected [1, 3]
    print(sol.twoRepeated([1, 2, 2, 1]))        # Expected [2, 1]
