# 암호 해독
# https://school.programmers.co.kr/learn/courses/30/lessons/120892

def solution(cipher, code):
    return cipher[code - 1::code]
