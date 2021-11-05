class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            ret = int(str(x)[::-1])
        else:
            ret = -int(str(x*-1)[::-1])
            
        if ret not in range (-2**31, 2**31):
            ret = 0
        
        return ret
