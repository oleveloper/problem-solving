# 옹알이 (2)
# https://school.programmers.co.kr/learn/courses/30/lessons/133499

def solution(babbling):
    answer = 0
    
    for b in babbling:
        p = ""
        while len(b) > 0:
            if b.startswith("aya") and p != "aya":
                b = b[3:]
                p = "aya"
            elif b.startswith("ye") and p != "ye":
                b = b[2:]
                p = "ye"
            elif b.startswith("woo") and p != "woo":
                b = b[3:]
                p = "woo"
            elif b.startswith("ma") and p != "ma":
                b = b[2:]
                p = "ma"
            else: break
            if len(b) == 0: answer += 1
            
    return answer
