# 배열 회전시키기
# https://school.programmers.co.kr/learn/courses/30/lessons/120844

def solution(numbers, direction):
    return numbers[-1:] + numbers[:-1] if direction == "right" else numbers[1:] + numbers[:1]
