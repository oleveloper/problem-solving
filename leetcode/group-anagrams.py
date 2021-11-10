class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        
        for word in strs:
            l = list(word)
            ls = sorted(l)
            lsw = str(ls)
            if lsw not in d:
                d[lsw] = [word]
            else:
                d[lsw].append(word)
        
        return list(d.values())
