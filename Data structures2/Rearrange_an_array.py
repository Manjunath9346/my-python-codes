class Solution:
    def arrange(self, arr):
        n = len(arr)
        
        # Step 1: Encode both old and new values into arr[i]
        for i in range(n):
            arr[i] += (arr[arr[i]] % n) * n
        
        # Step 2: Decode new values
        for i in range(n):
            arr[i] //= n

# Test Cases
print(non_repeating_character("hello"))   # Expected: 'h' (first non-repeating)
print(non_repeating_character("aabbcc"))  # Expected: '$' (no non-repeating char)
print(non_repeating_character("geeks"))   # Expected: 'g'
print(non_repeating_character("swiss"))   # Expected: 'w'
print(non_repeating_character("abcd"))    # Expected: 'a' (all unique → return first one)
