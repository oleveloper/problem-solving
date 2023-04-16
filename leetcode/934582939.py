# Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/submissions/934582939/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3: return n
        dp = [i for i in range(n + 1)]

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
