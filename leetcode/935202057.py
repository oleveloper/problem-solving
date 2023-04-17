# Single Number
# https://leetcode.com/problems/single-number/submissions/935202057/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i) == 1: return i
