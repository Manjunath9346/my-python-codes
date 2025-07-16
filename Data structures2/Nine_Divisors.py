import math

class Solution:
    def countNumbers(self, n):
        def sieve(limit):
            is_prime = [True] * (limit + 1)
            is_prime[0] = is_prime[1] = False
            for i in range(2, int(limit**0.5) + 1):
                if is_prime[i]:
                    for j in range(i*i, limit+1, i):
                        is_prime[j] = False
            return [i for i, val in enumerate(is_prime) if val]

        primes = sieve(int(n**0.5) + 1)
        count = 0

        # Case 1: p^8
        for p in primes:
            if p**8 <= n:
                count += 1
            else:
                break

        # Case 2: p^2 * q^2
        for i in range(len(primes)):
            p2 = primes[i] ** 2
            if p2 > n:
                break
            for j in range(i+1, len(primes)):
                q2 = primes[j] ** 2
                val = p2 * q2
                if val <= n:
                    count += 1
                else:
                    break

        return count
sol = Solution()
print(sol.countNumbers(100))    # ➞ 2  (36, 100)
print(sol.countNumbers(200))    # ➞ 3  (36, 100, 196)
print(sol.countNumbers(1000))   # ➞ 9
