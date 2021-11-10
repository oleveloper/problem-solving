class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40,"X":10,"IX":9,"V":5,"IV":4,"I":1}
        ret = 0
        l = 0
        
        for i, x in enumerate(s):
            if l + 1 < len(s) and s[l] + s[l+1] in d:
                ret += d.get(s[l] + s[l+1])
                l += 1
            elif l + 1 <= len(s):
                ret += d.get(s[l])
            l += 1
        
        return ret
