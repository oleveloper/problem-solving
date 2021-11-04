class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:        
        maxcnt = 0
        l1 = []
        l2 = []

        for x in str(s):
            if l1.count(x) > 0 :
                if len(l1) > len(l2):
                    l2 = l1
                    
                l1 = l1[l1.index(x) + 1 : ]                
                l1.append(x)

            else : 
                l1.append(x)
            
                if len(l1) > len(l2):
                    maxcnt = len(l1)
                else :
                    maxcnt = len(l2)

        return maxcnt
