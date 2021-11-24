class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        retval = 0
        xb = format(x, '032b')
        yb = format(y, '032b')
        
        for i in range(32):
            if xb[i] != yb[i]:
                retval += 1
                
        return retval
