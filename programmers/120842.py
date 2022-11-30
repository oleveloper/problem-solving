# 2차원으로 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/120842

def solution(num_list, n):
    return [num_list[x:x+n] for x in range(0, len(num_list), n)]
