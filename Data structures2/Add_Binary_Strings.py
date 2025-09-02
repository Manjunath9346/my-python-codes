# User function Template for python3
class Solution:
    def addBinary(self, s1, s2):
        # Convert binary strings to integers, add them, then convert back to binary string (removing '0b' prefix)
        return bin(int(s1, 2) + int(s2, 2))[2:]
obj = Solution()

print(obj.addBinary("1101", "111"))     # Output: "10100"
print(obj.addBinary("00100", "010"))    # Output: "110"
print(obj.addBinary("0", "0"))          # Output: "0"
print(obj.addBinary("1", "0"))          # Output: "1"
print(obj.addBinary("1010", "1011"))    # Output: "10101"
