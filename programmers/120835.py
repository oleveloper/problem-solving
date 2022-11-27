# 진료순서 정하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120835

def solution(emergency):
    answer = [-1 for x in range(len(emergency))]
    for i, v in enumerate(sorted(emergency, reverse=True)):
        answer[emergency.index(v)] = i + 1
    
    return answer
