class Solution:
    def isValid(self, s: str) -> bool:
        paren = {')':'(', '}':'{', ']':'['}
        stack = []
        
        for x in s:
            if x not in paren:
                stack.append(x)
            else:
                if stack and paren.get(x) == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        if stack:
            return False
        
        return True
