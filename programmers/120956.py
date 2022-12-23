# 옹알이 (1)
# https://school.programmers.co.kr/learn/courses/30/lessons/120956

import re

def solution(babbling):
    answer = 0
    
    for b in babbling:
        if re.fullmatch("(aya|ye|woo|ma)+", b): answer += 1
    
    return answer
