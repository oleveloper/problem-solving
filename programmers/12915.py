# 문자열 내 마음대로 정렬하기
# https://programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    answer = []
    tmp = []

    for i, v in enumerate(strings):
        tmp.append([i, v[n], v])
    
    tmp.sort(key=lambda x:(x[1],x[2]))
    answer = [x[2] for x in tmp]

    return answer
