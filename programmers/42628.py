# 이중우선순위큐
# https://programmers.co.kr/learn/courses/30/lessons/42628

def solution(operations):
    answer = []
    
    for oper in operations:
        cmd = oper.split(' ')
        if cmd[0] == 'I': 
            answer.append(int(cmd[1]))
        elif len(answer) > 0:
            if cmd[1][0] == '-': answer.remove(min(answer))
            else: answer.remove(max(answer))
    
    if len(answer) == 0: answer = [0, 0]
    else : answer = [max(answer), min(answer)]
    
    return answer
