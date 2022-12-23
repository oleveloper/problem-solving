# 할인 행사
# https://school.programmers.co.kr/learn/courses/30/lessons/131127

def solution(want, number, discount):
    answer = 0
    d = dict(zip(want, number))
    
    for i in range(0, len(discount) - 9):
        l = discount[i : i + 10]
        flag = True
        for j in d:
            if l.count(j) != d[j]: 
                flag = False
                break
        if flag: 
            answer += 1

    return answer
