class Solution:
    def getLastDigit(self, a, b):
        if b == "0": 
            return 1  # any number power 0 is 1

        last_digit_a = int(a[-1])
        
        # If last digit is 0, 1, 5, or 6 — it always remains the same
        if last_digit_a in [0, 1, 5, 6]:
            return last_digit_a

        # Determine the cycle of last digits
        cycle = []
        cur = last_digit_a
        while cur not in cycle:
            cycle.append(cur)
            cur = (cur * last_digit_a) % 10
        
        # Get the exponent mod cycle length
        exp = 0
        for ch in b:
            exp = (exp * 10 + int(ch)) % len(cycle)
        
        # Handle mod = 0 case (take last element of cycle)
        return cycle[exp - 1]
print(Solution().getLastDigit("3", "10"))     # Output: 9
print(Solution().getLastDigit("6", "2"))      # Output: 6
print(Solution().getLastDigit("7", "256"))    # Output: 9
print(Solution().getLastDigit("12", "15"))    # Output: 8
print(Solution().getLastDigit("9", "7"))      # Output: 9
print(Solution().getLastDigit("2", "1000"))   # Output: 6
print(Solution().getLastDigit("10", "0"))     # Output: 1
