class Solution(object):
    def twoSum(self, nums, target):
         for xi, xv in enumerate(nums):
             for yi, yv in enumerate(nums):
                 if xi != yi and xv + yv == target : 
                    return ([xi, yi])
