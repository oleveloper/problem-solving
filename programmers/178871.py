# 달리기 경주
# https://school.programmers.co.kr/learn/courses/30/lessons/178871

def solution(players, callings):
    d1 = { i : v for i, v in enumerate(players) }
    d2 = { v : i for i, v in enumerate(players) }

    for called_name in callings:
        called_idx = d2.get(called_name)
        prev_idx = called_idx - 1
        prev_name = d1.get(prev_idx)
        
        d1[called_idx] = prev_name
        d1[prev_idx] = called_name
        
        d2[called_name] -= 1
        d2[prev_name] += 1
    
    return list(d1.values())
