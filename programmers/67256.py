# [카카오 인턴] 키패드 누르기
# https://programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    answer = ''
    d = {1: 'L', 4: 'L', 7: 'L', 3: 'R', 6: 'R', 9: 'R'}
    li = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    l, r = (3, 0), (3, 2)
    
    for n in numbers:
        if n in d: answer += d[n]
        else: 
            tmp = [(i,j) for i in range(4) for j in range(3) if li[i][j]==n][0]
            x1, y1, x2, y2 = abs(tmp[0] - l[0]), abs(tmp[1] - l[1]), abs(tmp[0] - r[0]), abs(tmp[1] - r[1])
            if y1 + x1 == y2 + x2:
                answer += hand[0].upper()
            elif (x1, y1) < (x2, y2):
                answer += 'L'
            else:
                answer += 'R'
        
        if answer[-1] == 'L':
            l = [(i,j) for i in range(4) for j in range(3) if li[i][j] == n][0]
        else:
            r = [(i,j) for i in range(4) for j in range(3) if li[i][j] == n][0]
            
    return answer
