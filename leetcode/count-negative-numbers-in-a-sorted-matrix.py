# 1351. Count Negative Numbers in a Sorted Matrix

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return len([y for x in grid for y in x if 0 > y])
