# 최댓값과 최솟값
# https://programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    answer = ''
    
    l = s.split(' ')
    l = [int(x) for x in l]
    
    answer += str(min(l)) + " " + str(max(l))
    return answer
