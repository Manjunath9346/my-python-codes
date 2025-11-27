class Solution:
    def sieve(self, n):
        if n < 2:
            return []

        prime = [True] * (n + 1)
        prime[0] = prime[1] = False
        
        p = 2
        while p * p <= n:
            if prime[p]:
                for i in range(p*p, n+1, p):
                    prime[i] = False
            p += 1
        
        return [i for i in range(2, n+1) if prime[i]]
Input:
10

Output:
[2, 3, 5, 7]
Input:
35

Output:
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
