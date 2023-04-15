# Add Binary
# https://leetcode.com/problems/add-binary/submissions/934118053/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a, 2) + int(b, 2)))[2:]
