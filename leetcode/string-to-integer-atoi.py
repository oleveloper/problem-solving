class Solution:
    def myAtoi(self, s: str) -> int:
        retval = 0
        signflag = False
        negative = False
        floatflag = False

        token = s.lstrip().split(' ')[0]
        
        if len(token) == 0 or len(token) == 1 and token[0].isdigit() == False or token[0].isdigit() == False and token[1].isdigit() == False:
            return 0
        
        for idx, x in enumerate(token):
            if idx == 0 and x == '-' and signflag == False:
                signflag = True
                negative = True
                
            elif idx == 0 and x == '+' and signflag == False :
                signflag = True
            
            elif x == '.':
                floatflag = True
        
            elif x.isdigit() == False:
                if idx == 0:
                    return 0
                
                token = token [:idx]
                break
        
        token = token.lstrip('-').lstrip('+').lstrip('0')
        if len(token) == 0:
            return 0
        retval = int(float(token))
        
        if negative:
            retval = -1 * int(retval)
        
        if retval > 2**31 - 1:
            retval = 2**31 - 1
        elif retval < -2**31:
            retval = -2**31
        
        return retval
