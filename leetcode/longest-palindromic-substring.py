class Solution:
    def longestPalindrome(self, s: str) -> str:
        l, j = 0, 0
        
        if len(s) <= 1:
            return s
        
        for i in range(len(s)):
            if s[i-l : i+1] == s[i-l : i+1][::-1]:
                l, j = l+1, i-l
            elif i - l > 0 and s[i-l-1 : i+1] == s[i-l-1 : i+1][::-1]:
                l, j = l+2, i-l-1
        
        return s[j : j + l]
