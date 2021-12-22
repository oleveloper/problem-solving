# 전화번호 목록
# https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    l = list(sorted(phone_book))
    d = {}
    
    for i in range(len(l)):
        d[l[i]] = 0
        if i + 1 < len(l) and l[i + 1][:len(l[i])] in d: return False

    return True
