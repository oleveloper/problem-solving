# 호텔 대실
# https://school.programmers.co.kr/learn/courses/30/lessons/155651

from heapq import heappop, heappush 

def solution(book_time):
    answer = 1
    h = []
    book_time = [(int(start[:2]) * 60 + int(start[3:]), int(end[:2]) * 60 + int(end[3:])) \
                 for start, end in sorted(book_time, key = lambda x:x[0])]

    for s, e in book_time:
        if not h:
            heappush(h, e)
            continue
        if h[0] <= s:
            heappop(h)
        else:
            answer += 1
        heappush(h, e + 10)
    
    return answer
