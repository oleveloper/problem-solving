# 다음에 올 숫자
# https://school.programmers.co.kr/learn/courses/30/lessons/120924

def solution(common):
    return common[-1] + common[1] - common[0] if common[1] - common[0] == common[2] - common[1] else (common[1] // common[0]) * common[-1]
