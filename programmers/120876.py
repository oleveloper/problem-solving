# 겹치는 선분의 길이
# https://school.programmers.co.kr/learn/courses/30/lessons/120876

def solution(lines):
    line = [set(range(l, r)) for l, r in lines]
    return len(line[0] & line[1] | line[1] & line[2] | line[0] & line[2])
