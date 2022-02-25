# [1차] 캐시
# https://programmers.co.kr/learn/courses/30/lessons/17680

def solution(cacheSize, cities):
    answer = 0
    cache = []
    
    if cacheSize == 0:
        return len(cities) * 5
    
    for city in cities:
        c = city.lower()
        if c in cache[-cacheSize:]:
            answer += 1
            while c in cache: cache.remove(c)
        else:
            answer += 5
        cache.append(c)

    return answer
