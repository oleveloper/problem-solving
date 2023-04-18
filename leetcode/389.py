# Find the Difference
# https://leetcode.com/problems/find-the-difference/description/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        l = list(t)
        for c in s:
            l.remove(c)

        return ''.join(l)
