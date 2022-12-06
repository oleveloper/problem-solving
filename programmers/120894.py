# 영어가 싫어요
# https://school.programmers.co.kr/learn/courses/30/lessons/120894

def solution(numbers):
    answer, s = "", ""
    d = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    
    for x in numbers:
        s += x
        if s in d:
            answer += str(d.get(s))
            s = ""
    
    return int(answer)
