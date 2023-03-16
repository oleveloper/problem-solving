# 단어 변환
# https://school.programmers.co.kr/learn/courses/30/lessons/43163

from collections import deque

def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append([begin, 0])
    check = [0] * len(words)
    
    while q:
        word, count = q.popleft()
        if word == target:
            return count
        
        for i in range(len(words)):
            diff = 0
            if not check[i]:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        diff += 1
                
                if diff == 1:
                    q.append([words[i], count + 1])
                    check[i] = 1
                
    return answer
