# Valid Anagram
# https://leetcode.com/problems/valid-anagram/submissions/935206588/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(list(s)) == sorted(list(t))
