from itertools import combinations

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {}
        btn = 2
        cnt = 3
        
        if digits == "":
            return []
        
        for x in range(97, 123):
            if cnt < 1:
                btn += 1
                if btn == 7 or btn == 9:
                    cnt = 3
                else:
                    cnt = 2
            else:
                cnt -= 1
            
            if btn in d:
                d.get(btn).append(chr(x))
            else:
                d[btn] = [chr(x)]
        
        li = []
        for x in digits:
            li += [d.get(int(x))]
        
        ret = []
        for x in list(product(*li)):
            ret.append(''.join(x))
        
        return ret
