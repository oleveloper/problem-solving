class Solution:
    def tribonacci(self, n: int) -> int:
        # Time Limit Exceeded
        #
        # if n <= 0:
        #     return 0
        # elif n <= 2:
        #     return 1
        # else:
        #     return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        
        t0, t1, t2 = 0, 1, 1
        
        if n <= 0:
            return 0
        elif n <= 2:
            return 1
        
        for i in range(3, n + 1):
            tn = t0 + t1 + t2
            t0 = t1
            t1 = t2
            t2 = tn
            
        return tn
