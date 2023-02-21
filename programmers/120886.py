# A로 B 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/120886

def solution(before, after):
    before_list = sorted(list(before))
    after_list = sorted(list(after))
    
    return 1 if before_list == after_list else 0
