# 두 개 뽑아서 더하기
# https://programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):
    answer = []
    
    for i, v in enumerate(numbers):
        r = len(numbers) - 1
        while i < r:
            answer.append(numbers[i] + numbers[r])
            r -= 1

    answer = sorted(list(set(answer)))
    return answer
