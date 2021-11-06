class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)
        minval = 0
        tmp = ""
        flag = True
        
        for idx, pre in enumerate(shortest):
            tmp += pre
            flag = True
            for cnt, word in enumerate(strs):
                if word[:idx + 1] == tmp and flag and cnt == len(strs) - 1:
                    minval = idx + 1
                elif word[:idx + 1] != tmp:
                    flag = False
                    
        return shortest[:minval]
