# 한 번만 등장한 문자
# https://school.programmers.co.kr/learn/courses/30/lessons/120896

def solution(s):
    return ''.join(sorted([c for c in s if s.count(c) == 1]))
